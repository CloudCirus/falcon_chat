import pytest

from chat.application.services import MessageService
from chat.application.dataclasses import Message


@pytest.fixture(scope="function")
def service(message_repo, users_repo, chat_repo):
    return MessageService(message_repo=message_repo, user_repo=users_repo, chat_repo=chat_repo)


def test__add(service, message_repo, message_1_dto, message_1):
    message = {
        "user_id": 1,
        "chat_id": 1,
        "text": "some_text_1"
    }
    message = service.add(**message)
    assert message == Message(
        user_id=1,
        chat_id=1,
        text='some_text_1',
        created_at=message.created_at,
        id=3
    )


def test__get_all(service, message_repo):
    chat_id = 1
    user_id = 1
    messages = service.get_all(chat_id, user_id)
    assert isinstance(messages, list) and bool(messages)
