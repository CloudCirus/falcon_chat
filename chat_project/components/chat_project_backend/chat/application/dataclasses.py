from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    auth: Optional[str] = None


class Chat(BaseModel):
    id: int
    title: str
    info: str
    owner: int
    members: List[int]


class ChatPart(BaseModel):
    id: int
    title: str
    info: str


class Message(BaseModel):
    id: int
    user_id: int
    chat_id: int
    text: str
