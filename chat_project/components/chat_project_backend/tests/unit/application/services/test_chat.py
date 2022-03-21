import pytest

from chat.adapters.database import repositories
from chat.application.services import ChatService, Chat
from tests.unit.application import storage_for_test


@pytest.fixture(scope="function")
def users():
    users = storage_for_test.Storage.users
    return users


@pytest.fixture(scope="function")
def chats():
    chats = storage_for_test.Storage.chats
    return chats


@pytest.fixture(scope="function")
def service(message_repo, users, chat_repo, chats):
    service = ChatService(
        user_repo=repositories.UserRepo(users=users),
        chat_repo=repositories.ChatRepo(chats=chats, users=users)
    )
    return service


def test__create(service):
    chat_part = {
        "title": "chat_test",
        "info": "info_test",
        "user_id": 1
    }
    assert service.create(**chat_part) == Chat(
        id=4,
        title='chat_test',
        info='info_test',
        user_id=1,
        members=[1]
    )


def test__get_info(service):
    chat_id = 1
    user_id = 1
    assert service.get_info(chat_id, user_id) == Chat(
        id=1,
        title='chat1',
        info='chat1_info',
        user_id=1,
        members=[1, 3]
    )


def test__change_info(service):
    chat_part = {
        "title": "chat_mod",
        "info": "chat1_info_mod",
        "user_id": 1,
        "id": 1
    }
    assert service.change_info(**chat_part) == Chat(
        id=1,
        title='chat_mod',
        info='chat1_info_mod',
        user_id=1,
        members=[1, 3]
    )


def test__add_user(service):
    chat_id = 1
    user_id = 1
    add_user_id = 2
    assert isinstance(service.add_user(chat_id, user_id, add_user_id), Chat)


def test__leave_chat(service):
    chat_id = 2
    user_id = 2
    assert service.leave_chat(chat_id, user_id) == Chat(
        id=2,
        title='chat2',
        info='chat2_info',
        user_id=2,
        members=[2, 3]
    )


def test__remove_user(service):
    chat_id = 1
    user_id = 1
    kick_user_id = 3
    assert isinstance(service.remove_user(chat_id, user_id, kick_user_id), Chat)


def test__remove_chat(service):
    chat_id = 3
    user_id = 3
    assert isinstance(service.remove_chat(chat_id, user_id), Chat)
