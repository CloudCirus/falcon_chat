from abc import ABC, abstractmethod
from typing import List, Optional

from .dataclasses import Chat, ChatPart, Message, User


class UserRepo(ABC):

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[dict]:
        ...

    @abstractmethod
    def get_by_username(self, username: str) -> Optional[dict]:
        ...

    @abstractmethod
    def add(self, user_payload: dict) -> Optional[str]:
        ...

    @abstractmethod
    def delete(self, user_id) -> Optional[User]:
        ...


class ChatRepo(ABC):

    @abstractmethod
    def get_chat(self, chat_id: int) -> Optional[dict]:
        ...

    @abstractmethod
    def create(self, chat: ChatPart) -> Chat:
        ...

    @abstractmethod
    def get_info(self, chat_id: int) -> Optional[Chat]:
        ...

    @abstractmethod
    def change_info(self, chat_info: ChatPart) -> Optional[Chat]:
        ...

    @abstractmethod
    def remove_by_id(self, chat_id: int) -> Optional[Chat]:
        ...

    @abstractmethod
    def add_user(self, chat_id: int, user_id: int) -> Optional[Chat]:
        ...

    @abstractmethod
    def remove_user(self, chat_id: int, user_id: int) -> Optional[Chat]:
        ...

    @abstractmethod
    def leave_chat(self, chat_id: int, user_id: int) -> Optional[Chat]:
        ...


class MessageRepo(ABC):

    @abstractmethod
    def get_all(self, chat_id: int, user_id: int) -> Optional[List[Message]]:
        ...

    @abstractmethod
    def add(self, chat: Message) -> Optional[Message]:
        ...
