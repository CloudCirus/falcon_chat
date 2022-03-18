import falcon
from classic.components import component
from falcon import Request, Response

from chat.application import services


@component
class Chats:
    chat: services.ChatService

    def on_post_create_chat(self, request: Request, response: Response):
        resp = self.chat.create(**request.media)
        response.body = resp.json()

    def on_get_chat_info(self, request: Request, response: Response):
        info = self.chat.get_info(request.params.get("id"))
        response.body = info.json()

    def on_post_chat_info(self, request: Request, response: Response):
        self.chat.change_info(**request.media)
