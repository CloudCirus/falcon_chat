import datetime
from typing import List, Optional

from classic.app import DTO, validate_with_dto
from classic.components import component
from pydantic import validate_arguments

from . import errors, interfaces
from .dataclasses import Chat, ChatPart, Message, User


class UserInfo(DTO):
    username: str
    password: Optional[str] = None
    id: Optional[int] = None


class ChatInfo(DTO):
    id: int
    title: str
    info: str
    owner: int
    members: List[int]


class ChatPartInfo(DTO):
    id: Optional[int] = None
    user_id: Optional[int] = None
    title: str
    info: str


class MessageInfo(DTO):
    user_id: int
    chat_id: int
    created_at: Optional[str] = None
    text: Optional[str] = None
    id: Optional[int] = None


@component
class UserService:
    user_repo: interfaces.UserRepo

    @validate_with_dto
    def add_user(self, user: UserInfo) -> Optional[tuple]:
        user = user.create_obj(User)
        if not self.user_repo.get_by_username(user.username):
            user_for_resp = self.user_repo.add(user)
            user_for_resp[1].password = None
            return user_for_resp
        else:
            raise errors.UsernameExistError()

    @validate_arguments
    def delete_user(self, user_id: int, curr_user_id: int) -> Optional[User]:
        if user_id != curr_user_id:
            raise errors.UserAccessError()
        if self.user_repo.get_by_id(user_id):
            user = self.user_repo.delete(user_id)
            user.password = None
            return user


@component
class ChatService:
    chat_repo: interfaces.ChatRepo
    user_repo: interfaces.UserRepo

    @validate_with_dto
    def create(self, chat_info: ChatPartInfo) -> Chat:
        chat = chat_info.create_obj(ChatPart)
        return self.chat_repo.create(chat)

    @validate_arguments
    def get_info(self, chat_id: int, user_id: int) -> Optional[Chat]:
        chat: dict = self.chat_repo.get_chat(chat_id)
        if not chat:
            raise errors.NoChatError(id=chat_id)
        if user_id not in chat.get("members"):
            raise errors.AccessError()
        info: Chat = self.chat_repo.get_info(chat_id)
        if info:
            return info
        else:
            raise errors.NoChatError(id=chat_id)

    @validate_with_dto
    def change_info(self, chat_info: ChatPartInfo) -> Optional[Chat]:
        chat_part = chat_info.create_obj(ChatPart)
        chat: dict = self.chat_repo.get_chat(chat_info.id)
        if not chat:
            raise errors.NoChatError(id=chat_info.id)
        if chat_info.user_id == chat.get("user_id"):
            return self.chat_repo.change_info(chat_part)
        else:
            raise errors.AccessError()

    @validate_arguments
    def remove_chat(self, chat_id: int, user_id: int) -> Optional[Chat]:
        chat: dict = self.chat_repo.get_chat(chat_id)
        if not chat:
            raise errors.NoChatError(id=chat_id)
        if user_id == chat.get("user_id"):
            return self.chat_repo.remove_by_id(chat_id)
        else:
            raise errors.AccessError()

    @validate_arguments
    def leave_chat(self, chat_id: int, user_id: int) -> Optional[Chat]:
        chat: dict = self.chat_repo.get_chat(chat_id)
        if not chat:
            raise errors.NoChatError(id=chat_id)
        if user_id not in chat.get("members"):
            raise errors.AccessError()
        if chat.get("user_id") == user_id:
            return self.chat_repo.remove_by_id(chat_id)
        return self.chat_repo.leave_chat(chat_id, user_id)

    @validate_arguments
    def remove_user(self, chat_id: int, user_id: int, kick_user_id: int) -> Optional[Chat]:
        chat: dict = self.chat_repo.get_chat(chat_id)
        if not chat:
            raise errors.NoChatError(id=chat_id)
        if kick_user_id not in chat.get("members"):
            raise errors.MemberError()
        if user_id == kick_user_id:
            return self.chat_repo.remove_by_id(chat_id)
        if chat.get("user_id") == user_id:
            return self.chat_repo.remove_user(chat_id, kick_user_id)

    @validate_arguments
    def add_user(self, chat_id: int, user_id: int, add_user_id: int) -> Chat:
        chat: dict = self.chat_repo.get_chat(chat_id)
        if not chat:
            raise errors.NoChatError(id=chat_id)
        if add_user_id in chat.get("members") or user_id == add_user_id:
            raise errors.MemberError()
        if not self.user_repo.get_by_id(add_user_id):
            raise errors.NoUserIdError(id=add_user_id)
        if chat.get("user_id") == user_id:
            return self.chat_repo.add_user(chat_id, add_user_id)


@component
class MessageService:
    message_repo: interfaces.MessageRepo
    user_repo: interfaces.UserRepo
    chat_repo: interfaces.ChatRepo

    @validate_arguments
    def get_all(self, chat_id: int, user_id: int) -> Optional[List[Message]]:
        messages = self.message_repo.get_all(chat_id, user_id)
        if messages:
            return messages
        else:
            raise errors.AccessError()

    @validate_with_dto
    def add(self, message: MessageInfo) -> Optional[Message]:
        time = datetime.datetime.now()
        created_at = time.strftime("%d.%m.%Y %H:%M")
        message.created_at = created_at
        message = message.create_obj(Message)
        chat = self.chat_repo.get_chat(message.chat_id)
        if chat:
            if message.user_id in chat.get("members"):
                return self.message_repo.add(message)
            else:
                raise errors.AccessError()
        else:
            raise errors.NoChatError(id=message.chat_id)
