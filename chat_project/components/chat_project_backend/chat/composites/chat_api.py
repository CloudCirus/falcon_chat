# from sqlalchemy import create_engine
#
# from classic.sql_storage import TransactionContext
#
from chat.adapters import database, chat_api
from chat.adapters.database.storage import Storage
from chat.application import services


class Settings:
    # db = database.Settings()
    shop_api = chat_api.Settings()


# class Logger:
#     log.configure(
#         # Settings.db.LOGGING_CONFIG,
#         Settings.chat_api.LOGGING_CONFIG,
#     )


#
#
class DB:
    # engine = create_engine(Settings.db.DB_URL)
    # database.metadata.create_all(engine)

    # context = TransactionContext(bind=engine)

    chat_repo = database.repositories.ChatRepo(chats=Storage.users)
    # products_repo = database.repositories.ProductsRepo(context=context)
    # carts_repo = database.repositories.CartsRepo(context=context)
    # orders_repo = database.repositories.OrdersRepo(context=context)


#
#
# class MailSending:
#     sender = mail_sending.FileMailSender()
#
#
class Application:
    chat = services.ChatService(chat_repo=DB.chat_repo)
    # checkout = services.(
    #     customers_repo=DB.customers_repo,
    #     products_repo=DB.products_repo,
    #     carts_repo=DB.carts_repo,
    #     orders_repo=DB.orders_repo,
    # )
    # orders = services.Orders(
    #     orders_repo=DB.orders_repo,
    #     mail_sender=MailSending.sender,
    # )
    # customers = services.Customers(customers_repo=DB.customers_repo)

    # is_dev_mode = Settings.chat_api.IS_DEV_MODE
    # allow_origins = Settings.chat_api.ALLOW_ORIGINS


#
#
# class Aspects:
#     services.join_points.join(DB.context)
#     chat_api.join_points.join(DB.context)
#
#
app = chat_api.create_app(

    chat=Application.chat,
    # is_dev_mode=Application.is_dev_mode,
    # allow_origins=Application.allow_origins,
    # checkout=Application.checkout,
    # orders=Application.orders,
    # customers=Application.customers,
)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    with make_server('localhost', 2022, app) as http_server:
        print('server started')
        http_server.serve_forever(0.1)
