from chat.adapters import chat_api, database
from chat.adapters.database.storage import Storage
from chat.application import services


class Settings:
    shop_api = chat_api.Settings()


class DB:
    chat_repo = database.repositories.ChatRepo(chats=Storage.chats)
    # user_repo = database.repositories.UserRepo(users=Storage.users)
    # message_repo = database.repositories.MessageRepo(messages=Storage.messages)


class Application:
    chat = services.ChatService(chat_repo=DB.chat_repo)


app = chat_api.create_app(
    chat=Application.chat,
)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    with make_server('localhost', 2022, app) as http_server:
        print('server started')
        http_server.serve_forever(0.1)
