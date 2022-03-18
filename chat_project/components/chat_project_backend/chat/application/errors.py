from classic.app.errors import AppError


class NoChat(AppError):
    msg_template = "No chat with '{id}'"
    code = 'chat.no_chat'


class CantCreateChat(AppError):
    msg_template = "Can't create chat with '{id}'"
    code = 'chat.cant_create_chat'


class NoOrder(AppError):
    msg_template = "No order with number '{number}'"
    code = 'shop.no_order'


class NoCustomer(AppError):
    msg_template = "No customer with id '{id}'"
    code = 'shop.no_customer'


class EmptyCart(AppError):
    msg_template = "Cart is empty"
    code = 'shop.cart_is_empty'
