from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    email: str
    first_name: str
    last_name: str


class UserCreate(UserBase):
    pass


class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class ChatBase(BaseModel):
    user1_id: int
    user2_id: int


class ChatOut(ChatBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class MessageBase(BaseModel):
    chat_id: int
    sender_id: int
    message: str


class MessageOut(MessageBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
