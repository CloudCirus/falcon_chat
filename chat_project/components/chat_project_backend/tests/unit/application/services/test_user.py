import pytest

from chat.application.services import UserService
from chat.application.dataclasses import User


@pytest.fixture(scope="function")
def service(user_repo):
    return UserService(user_repo=user_repo)


def test__add_user(service, user_repo):
    username = "user2"
    password = "user2"
    service.add_user(username=username, password=password)

    _, value = user_repo.add.return_value
    print(value)
    assert value == User(username=username, password=None, id=2)


def test__delete_user(service, user_repo, user_1):
    user_id = 1
    curr_user_id = 1
    service.delete_user(user_id, curr_user_id)
    value = user_repo.delete.return_value
    assert value == user_1
