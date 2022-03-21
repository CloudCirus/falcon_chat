from unittest.mock import Mock

import pytest

from chat.application import interfaces
from chat.adapters.database import repositories
import storage_for_test


@pytest.fixture(scope="function")
def user_repo(user_1, user_2):
    user_repo = Mock(interfaces.UserRepo)
    user_repo.add = Mock(return_value=("token", user_2))
    user_repo.get_by_username = Mock(return_value=None)
    user_repo.get_by_id = Mock(return_value=True)
    user_repo.delete = Mock(return_value=user_1)
    return user_repo


@pytest.fixture(scope="function")
def chat_storage():
    chats = storage_for_test.Storage.chats
    return chats


@pytest.fixture(scope="function")
def message_storage():
    return storage_for_test.Storage.messages


@pytest.fixture(scope="function")
def user_storage():
    return storage_for_test.Storage.users


@pytest.fixture(scope="function")
def message_repo():
    return repositories.MessageRepo(messages=storage_for_test.Storage.messages)


@pytest.fixture()
def users_repo():
    return repositories.UserRepo(users=storage_for_test.Storage.users)


@pytest.fixture()
def chat_repo():
    return repositories.ChatRepo(chats=storage_for_test.Storage.chats, users=storage_for_test.Storage.users)
