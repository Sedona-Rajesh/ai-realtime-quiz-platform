from fastapi import WebSocket, APIRouter

router = APIRouter()

@router.websocket("/ws/{quiz_code}")
async def quiz_websocket(websocket: WebSocket, quiz_code: str):
    await websocket.accept()
    await websocket.send_text(f"Connected to quiz {quiz_code}")
