from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/ws", tags=["WebSocket"])

connections = {}


@router.websocket("/chat/{chat_id}")
async def websocket_endpoint(websocket: WebSocket, chat_id: int, db: Session = Depends(database.get_db)):
    await websocket.accept()
    connections.setdefault(chat_id, []).append(websocket)

    try:
        while True:
            data = await websocket.receive_json()
            msg_data = schemas.MessageBase(**data)
            crud.create_message(db, msg_data)

            for conn in connections[chat_id]:
                await conn.send_json({"message": msg_data.message, "sender_id": msg_data.sender_id})
    except WebSocketDisconnect:
        connections[chat_id].remove(websocket)
