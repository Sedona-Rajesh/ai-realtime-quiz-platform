from fastapi import WebSocket, APIRouter

router = APIRouter()

# This stores quiz_code -> list of users
active_connections = {}

@router.websocket("/ws/{quiz_code}")
async def quiz_websocket(websocket: WebSocket, quiz_code: str):
    await websocket.accept()

    # Add user to quiz room
    if quiz_code not in active_connections:
        active_connections[quiz_code] = []

    active_connections[quiz_code].append(websocket)

    # Send confirmation
    await websocket.send_text(f"Joined quiz room {quiz_code}")

    try:
        while True:
            data = await websocket.receive_text()
            # (we'll handle messages later)
    except:
        # Remove user when disconnected
        active_connections[quiz_code].remove(websocket)
