from fastapi import WebSocket, APIRouter

router = APIRouter()

# quiz_code -> list of connected users
active_connections = {}

@router.websocket("/ws/{quiz_code}")
async def quiz_websocket(websocket: WebSocket, quiz_code: str):
    await websocket.accept()

    if quiz_code not in active_connections:
        active_connections[quiz_code] = []

    active_connections[quiz_code].append(websocket)

    await websocket.send_text(f"Joined quiz room {quiz_code}")

    try:
        while True:
            message = await websocket.receive_text()

            # Broadcast message to everyone in the quiz
            for connection in active_connections[quiz_code]:
                await connection.send_text(message)

    except:
        active_connections[quiz_code].remove(websocket)
