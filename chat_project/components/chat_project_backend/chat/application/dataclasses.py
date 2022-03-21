from dataclasses import dataclass
from typing import List, Optional


@dataclass
class User:
    username: str
    password: Optional[str]
    id: Optional[int] = None

@dataclass
class Chat:
    id: int
    title: str
    info: str
    user_id: int
    members: List[int]


@dataclass
class ChatPart:
    title: str
    info: str
    id: Optional[int] = None
    user_id: Optional[int] = None


@dataclass
class Message:
    user_id: int
    chat_id: int
    text: str
    created_at: str
    id: Optional[int] = None
