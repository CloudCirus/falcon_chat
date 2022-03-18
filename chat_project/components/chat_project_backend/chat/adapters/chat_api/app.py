from classic.http_api import App

from chat.application import services

from . import controllers


def create_app(
        chat: services.ChatService,
) -> App:
    middleware = []

    app = App(middleware=middleware, prefix='/api')

    app.register(controllers.Chats(chat=chat))

    return app
