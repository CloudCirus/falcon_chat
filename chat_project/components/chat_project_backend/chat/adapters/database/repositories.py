from typing import List, Optional

from classic.components import component

from chat.application import interfaces
from chat.application.dataclasses import Chat, ChatPart, Message, User

from .storage import Storage


@component
class UserRepo(interfaces.UserRepo):
    users: Storage.users

    def get_by_id(self, user_id: int) -> Optional[User]:
        for user in self.users:
            if user.get("id") == user_id:
                return User(**user)

    def add(self, user: User) -> None:
        self.users.append(user.dict())


@component
class ChatRepo(interfaces.ChatRepo):
    chats: Storage.chats

    def get_chat(self, chat_id: int) -> Optional[dict]:
        for chat in self.chats:
            if chat.get("id") == chat_id:
                return chat
        return None

    def create(self, chat: Chat) -> Optional[Chat]:
        validate = True
        if self.get_chat(chat.id):
            validate = False
        if validate:
            self.chats.append(chat.dict())
            return chat

    def get_info(self, chat_id: int) -> Optional[ChatPart]:
        chat = self.get_chat(chat_id)
        if chat:
            return ChatPart(
                id=chat.get("id"),
                title=chat.get("title"),
                info=chat.get("info")
            )

    def change_info(self, chat_info: ChatPart) -> None:
        for i, chat in enumerate(self.chats):
            if chat.get("id") == chat_info.id:
                self.chats[i].update(chat_info)

    def remove_by_id(self, chat_id: int) -> None:
        for i, chat in enumerate(self.chats):
            if chat.get("id") == chat_id:
                self.chats.pop(i)
                break

    def add_user(self, chat_id, user_id: int) -> None:
        for i, chat in enumerate(self.chats):
            if chat.get("id") == chat_id:
                value = self.chats[i]["members"]
                value.append(user_id)
                self.chats[i]["members"] = value

    def remove_user(self, chat_id: int, user_id: int) -> None:
        for i, chat in enumerate(self.chats):
            if chat.get("id") == chat_id:
                value = self.chats[i]["members"]
                value.remove(user_id)
                self.chats[i]["members"] = value


@component
class MessageRepo(interfaces.MessageRepo):
    chats = Storage.chats
    messages = Storage.messages

    def get_all(self, chat_id: int, user_id: int) -> Optional[List[Message]]:
        collection = []
        for message in self.messages:
            if message.get("user_id") == user_id and message.get("chat_id") == chat_id:
                collection.append(Message(**message))
                return collection

    def add(self, message: Message) -> None:
        validation = True
        for mess in self.messages:
            if mess.get("id") == message.id:
                validation = False
        if validation:
            self.messages.append(message.dict())
