import hashlib
from dataclasses import asdict
from typing import List, Optional

import jwt
from classic.components import component

from chat.application import interfaces
from chat.application.dataclasses import Chat, ChatPart, Message, User

from .storage import Storage


@component
class UserRepo(interfaces.UserRepo):
    users: Storage.users

    def get_by_id(self, user_id: int) -> Optional[dict]:
        for user in self.users:
            if user.get("id") == user_id:
                return user

    def get_by_username(self, username: str) -> Optional[dict]:
        for user in self.users:
            if user.get("username") == username:
                return user

    def add(self, user: User) -> Optional[tuple]:
        key = Storage.secret_key
        user_id = self.users[-1].get("id") + 1 if self.users else 1
        encoded_jwt = jwt.encode({"username": user.username, "id": user_id}, key=key, algorithm="HS256")
        password_hash = hashlib.sha256(user.password.encode()).hexdigest()
        user.id, user.password = user_id, password_hash
        print("created_user", user)
        self.users.append(asdict(user))
        return encoded_jwt, user

    def delete(self, user_id) -> Optional[User]:
        for i, user in enumerate(self.users):
            if user.get("id") == user_id:
                return User(**self.users.pop(i))


@component
class ChatRepo(interfaces.ChatRepo):
    chats: Storage.chats
    users: Storage.users

    def get_chat(self, chat_id: int) -> Optional[dict]:
        for chat in self.chats:
            if chat.get("id") == chat_id:
                return chat

    def create(self, chat_part: ChatPart) -> Chat:
        chat_entry = asdict(chat_part)
        chat_entry.update(
            {
                "id": self.chats[-1]["id"] + 1 if self.chats else 1,
                "user_id": chat_part.user_id,
                "members": [chat_part.user_id],
            }
        )
        self.chats.append(chat_entry)
        chat = Chat(**chat_entry)
        return chat

    def get_info(self, chat_id: int) -> Optional[Chat]:
        chat = self.get_chat(chat_id)
        if chat:
            return Chat(**chat)

    def change_info(self, chat_part: ChatPart) -> Optional[Chat]:
        for i, chat in enumerate(self.chats):
            if chat.get("id") == chat_part.id:
                self.chats[i].update(asdict(chat_part))
                return Chat(**chat)

    def remove_by_id(self, chat_id: int) -> Optional[Chat]:
        for i, chat in enumerate(self.chats):
            if chat.get("id") == chat_id:
                return Chat(**self.chats.pop(i))

    def add_user(self, chat_id: int, add_user_id: int) -> Optional[Chat]:
        for i, chat in enumerate(self.chats):
            if chat.get("id") == chat_id:
                value: list = self.chats[i]["members"]
                value.append(add_user_id)
                self.chats[i]["members"] = value
                return Chat(**chat)

    def remove_user(self, chat_id: int, kick_user_id: int) -> Optional[Chat]:
        for i, chat in enumerate(self.chats):
            if chat.get("id") == chat_id:
                value: list = self.chats[i]["members"]
                value.remove(kick_user_id)
                self.chats[i]["members"] = value
                return Chat(**chat)

    def leave_chat(self, chat_id: int, user_id: int) -> Optional[Chat]:
        for i, chat in enumerate(self.chats):
            if chat.get("id") == chat_id:
                members: list = chat.get("members")
                members.remove(chat_id)
                return Chat(**chat)


@component
class MessageRepo(interfaces.MessageRepo):
    messages: Storage.messages

    def get_all(self, chat_id: int, user_id: int) -> Optional[List[dict]]:
        collection = []
        for message in self.messages:
            if message.get("user_id") == user_id and message.get("chat_id") == chat_id:
                collection.append(asdict(Message(**message)))
        return collection

    def add(self, message: Message) -> Message:
        if self.messages:
            message_id = self.messages[-1].get("id")
        else:
            message_id = 1
        message.id = message_id
        self.messages.append(asdict(message))
        return message
