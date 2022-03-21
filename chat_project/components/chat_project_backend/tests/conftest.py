import pytest

from chat.application import dataclasses, services


@pytest.fixture(scope="function")
def user_2():
    return dataclasses.User(
        id=2,
        username="user2",
        password="5269ef980de47819ba3d14340f4665262c41e933dc92c1a27dd5d01b047ac80e"
    )


@pytest.fixture(scope="function")
def user_1():
    return dataclasses.User(
        id=1,
        username="user1",
        password=None
    )


@pytest.fixture(scope="function")
def chat_1():
    return dataclasses.Chat(
        id=1,
        title="some_chat_title_1",
        info="some_chat_info_1",
        user_id=1,
        members=[1, 2, 3]
    )


@pytest.fixture(scope="function")
def chat_2():
    return dataclasses.Chat(
        id=2,
        title="some_chat_title_2",
        info="some_chat_info_2",
        user_id=2,
        members=[1, 2, 3]
    )


@pytest.fixture(scope="function")
def chat_part_1():
    return dataclasses.ChatPart(
        id=1,
        title="some_chat_title_1",
        info="some_chat_info_1",
        user_id=1
    )


@pytest.fixture(scope="function")
def chat_part_2():
    return dataclasses.ChatPart(
        id=2,
        title="some_chat_title_2",
        info="some_chat_info_2",
        user_id=2
    )


@pytest.fixture(scope="function")
def message_1():
    return dataclasses.Message(
        id=1,
        chat_id=1,
        user_id=1,
        text="some_text_1",
        created_at="20.03.2022 21:33"
    )


@pytest.fixture(scope="function")
def message_1_dto():
    return services.MessageInfo(
        user_id=1,
        chat_id=1,
        created_at=None,
        text="some_text_1",
        id=None
    )


@pytest.fixture(scope="function")
def message_2():
    return dataclasses.Message(
        id=2,
        chat_id=2,
        user_id=2,
        text="some_text_2",
        created_at="20.03.2022 21:33"
    )
