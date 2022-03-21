from classic.app.errors import AppError


class NoChatError(AppError):
    msg_template = "No chat with '{id}'"
    code = "no_chat"


class AccessError(AppError):
    msg_template = "You cannot manage this chat"
    code = "access"


class MemberError(AppError):
    msg_template = "Cannot perform an operation with a chat member"
    code = "access"


class ChangeInfoError(AppError):
    msg_template = "You cannot manage this chat"
    code = "chat_part.cant_create_chat"


class DeleteChatError(AppError):
    msg_template = "You can not change info for this chat"
    code = "chat_part.cant_create_chat"


class AuthError(AppError):
    msg_template = "Auth problem, token invalid"
    code = "user_part.cant_auth_user"


class UsernameExistError(AppError):
    msg_template = "Username allready exist"
    code = "user_part.username_exist"


class NoUserIdError(AppError):
    msg_template = "No user with '{id}'"
    code = "user_part.no_id"


class UserAccessError(AppError):
    msg_template = "You cannot manage this user"
    code = "user_part.access"


class NoOrder(AppError):
    msg_template = "No order with number '{number}'"
    code = 'shop.no_order'


class NoCustomer(AppError):
    msg_template = "No customer with id '{id}'"
    code = 'shop.no_customer'


class EmptyCart(AppError):
    msg_template = "Cart is empty"
    code = 'shop.cart_is_empty'
