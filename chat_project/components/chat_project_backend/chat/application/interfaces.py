from abc import ABC, abstractmethod
from typing import List, Optional

from .dataclasses import Chat, ChatPart, Message, User


class UserRepo(ABC):

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        ...

    @abstractmethod
    def add(self, user: User):
        ...


class ChatRepo(ABC):

    @abstractmethod
    def create(self, chat: Chat) -> Chat:
        ...

    @abstractmethod
    def get_info(self, chat_id: int) -> ChatPart:
        ...

    @abstractmethod
    def change_info(self, chat_info: ChatPart) -> None:
        ...

    @abstractmethod
    def remove_by_id(self, chat_id: int) -> None:
        ...

    @abstractmethod
    def add_user(self, chat_id: int, user_id: int) -> None:
        ...

    @abstractmethod
    def remove_user(self, chat_id: int, user_id: int) -> None:
        ...


class MessageRepo(ABC):

    @abstractmethod
    def get_all(self, chat_id: int, user_id: int) -> Optional[List[Message]]:
        ...

    @abstractmethod
    def add(self, message: Message) -> None:
        ...
