from dataclasses import asdict

from classic.components import component
from falcon import Request, Response

from chat.application import services


@component
class Users:
    user: services.UserService

    def on_post_login(self, request: Request, response: Response):
        payload = {
            "username": request.media.get("username"),
            "password": request.media.get("password")
        }
        user: tuple = self.user.add_user(**payload)
        response.set_header("Authorization", user[0])
        response.media = {"add user": asdict(user[1])}

    def on_get_logout(self, request: Request, response: Response):
        curr_user_id = request.context.get("user_id")
        user_id = request.params.get("id")
        user = self.user.delete_user(user_id, curr_user_id)
        response.media = {"deleted": asdict(user)}


@component
class Chats:
    chat: services.ChatService

    def on_post_create_chat(self, request: Request, response: Response):
        user_id = request.context.get("user_id")
        request.media.update({"user_id": user_id})
        chat = self.chat.create(**request.media)
        response.media = asdict(chat)

    def on_get_chat_info(self, request: Request, response: Response):
        chat_id = request.params.get("id")
        user_id = request.context.get("user_id")
        info = self.chat.get_info(chat_id, user_id)
        response.media = asdict(info)

    def on_post_chat_info(self, request: Request, response: Response):
        payload = request.media
        user_id = request.context.get("user_id")
        payload.update({"id": request.params.get("id"), "user_id": user_id})
        response.media = asdict(self.chat.change_info(**payload))

    def on_get_remove_chat(self, request: Request, response: Response):
        user_id = request.context.get("user_id")
        chat_id = request.params.get("id")
        response.media = {"deleted": asdict(self.chat.remove_chat(chat_id, user_id))}

    def on_get_leave_chat(self, request: Request, response: Response):
        user_id = request.context.get("user_id")
        chat_id = request.params.get("id")
        response.media = {"leaved_from": asdict(self.chat.leave_chat(chat_id, user_id))}

    def on_post_remove_user(self, request: Request, response: Response):
        user_id = request.context.get("user_id")
        chat_id = request.params.get("id")
        kick_user_id = request.media.get("id")
        response.media = {"remove_user_from": asdict(self.chat.remove_user(chat_id, user_id, kick_user_id))}

    def on_post_add_user(self, request: Request, response: Response):
        user_id = request.context.get("user_id")
        chat_id = request.params.get("id")
        add_user_id = request.media.get("id")
        response.media = {"add_user_into": asdict(self.chat.add_user(chat_id, user_id, add_user_id))}


@component
class Messages:
    message: services.MessageService

    def on_get_all(self, request: Request, response: Response):
        user_id = request.context.get("user_id")
        chat_id = request.params.get("chat_id")
        response.media = self.message.get_all(chat_id, user_id)

    def on_post_add(self, request: Request, response: Response):
        user_id = request.context.get("user_id")
        chat_id = request.params.get("chat_id")
        text = request.media.get("text")
        payload = {
            "user_id": user_id,
            "chat_id": chat_id,
            "text": text,
        }
        response.media = asdict(self.message.add(**payload))
