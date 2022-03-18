from classic.components import component
from falcon import Request, Response
from chat.application import services


@component
class ChatController:
    chat: services.ChatService

    def on_post_create_chat(self, request: Request, response: Response):
        self.chat.create(**request.media)

    def on_get_chat_info(self, request: Request, response: Response):
        info = self.chat.get_info(request.media.get("id"))
        response.media = info

    def on_post_chat_info(self, request: Request, response: Response):
        self.chat.change_info(**request.media)
