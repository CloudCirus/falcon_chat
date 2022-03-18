from typing import List, Optional

from classic.app import DTO, validate_with_dto
from classic.components import component
from pydantic import conint, validate_arguments

from . import errors, interfaces
from .dataclasses import Chat, ChatPart, Message, User


class UserInfo(DTO):
    id: int
    username: str
    auth: Optional[str] = None


class ChatInfo(DTO):
    id: int
    title: str
    info: str
    owner: int
    members: List[int]


class ChatInfoForChange(DTO):
    id: int
    title: str
    info: str


class MessageInfo(DTO):
    user_id: int
    chat_id: int
    text: str


@component
class ChatService:
    chat_repo: interfaces.ChatRepo

    @validate_with_dto
    def create(self, chat_info: ChatInfo) -> Chat:
        chat = chat_info.create_obj(Chat)
        response = self.chat_repo.create(chat)
        if response:
            return response
        else:
            raise errors.CantCreateChat(id=chat_info.id)

    @validate_arguments
    def get_info(self, chat_id: int) -> ChatPart:
        info = self.chat_repo.get_info(chat_id)
        if info:
            return self.chat_repo.get_info(chat_id)
        else:
            raise errors.NoChat(id=chat_id)

    @validate_with_dto
    def change_info(self, chat_info: ChatInfoForChange) -> None:
        print("change chat info service")
        info = chat_info.create_obj(ChatInfo)
        self.chat_repo.change_info(info)
