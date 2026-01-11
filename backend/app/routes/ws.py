import json
import asyncio
from fastapi import WebSocket, APIRouter
from app.database import SessionLocal
from app.models.result import QuizResult

router = APIRouter()

active_connections = {}      # quiz_code -> [connections]
answers_store = {}           # quiz_code -> { user_id : option }
quiz_active = {}             # quiz_code -> True / False
scores = {}                  # quiz_code -> { user_id : score }

@router.websocket("/ws/{quiz_code}/{user_id}")
async def quiz_websocket(websocket: WebSocket, quiz_code: str, user_id: str):
    await websocket.accept()

    active_connections.setdefault(quiz_code, []).append(websocket)
    answers_store.setdefault(quiz_code, {})
    quiz_active.setdefault(quiz_code, False)
    scores.setdefault(quiz_code, {})
    scores[quiz_code].setdefault(user_id, 0)

    await websocket.send_text(json.dumps({
        "type": "status",
        "message": f"{user_id} joined quiz {quiz_code}"
    }))

    try:
        while True:
            message = await websocket.receive_text()
            data = json.loads(message)

            # HOST starts question
            if data["type"] == "start_question":
                quiz_active[quiz_code] = True
                answers_store[quiz_code] = {}
                correct_answer = data["correct_answer"]

                for conn in active_connections[quiz_code]:
                    await conn.send_text(json.dumps({
                        "type": "question",
                        "question_text": data["question_text"],
                        "options": data["options"],
                        "time": data["time"]
                    }))

                asyncio.create_task(
                    question_timer(quiz_code, data["time"], correct_answer)
                )

            # STUDENT submits answer
            elif data["type"] == "answer":
                if not quiz_active[quiz_code]:
                    print(f"[{quiz_code}] Answer rejected (time up)")
                    continue

                if user_id in answers_store[quiz_code]:
                    print(f"[{quiz_code}] {user_id} tried to answer again (ignored)")
                    continue

                answers_store[quiz_code][user_id] = data["selected_option"]
                print(f"[{quiz_code}] {user_id} answered {data['selected_option']}")

    except:
        active_connections[quiz_code].remove(websocket)


async def question_timer(quiz_code: str, seconds: int, correct_answer: str):
    await asyncio.sleep(seconds)
    quiz_active[quiz_code] = False

    db = SessionLocal()

    for user_id, answer in answers_store[quiz_code].items():
        if answer == correct_answer:
            scores[quiz_code][user_id] += 1

        
        result = QuizResult(
            quiz_code=quiz_code,
            user_id=user_id,
            score=scores[quiz_code][user_id]
        )
        db.add(result)

    db.commit()
    db.close()

    print(f"[{quiz_code}] SCORES SAVED:", scores[quiz_code])

    for conn in active_connections.get(quiz_code, []):
        await conn.send_text(json.dumps({
            "type": "leaderboard",
            "scores": scores[quiz_code],
            "correct_answer": correct_answer
        }))


