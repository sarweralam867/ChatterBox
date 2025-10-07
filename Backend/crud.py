from sqlalchemy.orm import Session
from . import models, schemas


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_all_users(db: Session):
    return db.query(models.User).all()


def create_chat(db: Session, user1_id: int, user2_id: int):
    chat = models.Chat(user1_id=user1_id, user2_id=user2_id)
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return chat


def get_chats_by_user(db: Session, user_id: int):
    return db.query(models.Chat).filter(
        (models.Chat.user1_id == user_id) | (models.Chat.user2_id == user_id)
    ).all()


def create_message(db: Session, msg: schemas.MessageBase):
    db_msg = models.Message(**msg.dict())
    db.add(db_msg)
    db.commit()
    db.refresh(db_msg)
    return db_msg


def get_messages(db: Session, chat_id: int):
    return db.query(models.Message).filter(models.Message.chat_id == chat_id).all()


def delete_chat(db: Session, chat_id: int):
    db.query(models.Message).filter(models.Message.chat_id == chat_id).delete()
    db.query(models.Chat).filter(models.Chat.id == chat_id).delete()
    db.commit()
