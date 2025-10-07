from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, database, schemas

router = APIRouter(prefix="/chats", tags=["Chats"])


@router.get("/{user_id}", response_model=list[schemas.ChatOut])
def get_chats(user_id: int, db: Session = Depends(database.get_db)):
    return crud.get_chats_by_user(db, user_id)


@router.delete("/{chat_id}")
def delete_chat(chat_id: int, db: Session = Depends(database.get_db)):
    crud.delete_chat(db, chat_id)
    return {"message": "Chat deleted"}
