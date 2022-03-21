from classic.http_api import App

from chat.application import services

from . import controllers
from .middleware import AuthComponent


def create_app(
        chat: services.ChatService,
        user: services.UserService,
        message: services.MessageService,
) -> App:
    middleware = [
        AuthComponent()
    ]

    app = App(middleware=middleware, prefix='/api')

    app.register(controllers.Chats(chat=chat))
    app.register(controllers.Users(user=user))
    app.register(controllers.Messages(message=message))

    return app
