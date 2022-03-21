from pprint import pprint


class Storage:
    secret_key = "some_secret_key"
    users = [
        {
            "id": 1,
            "username": "user1",
            "password": "_j7b4T34zMe3XoBwZG3NkE04CWInn1RxXWxTbE6D7Rc"
        },
        {
            "id": 2,
            "username": "user2",
            "password": None,
        },
        {
            "id": 3,
            "username": "user3",
            "password": None,
        }
    ]
    chats = [
        {
            "id": 1,
            "title": "chat1",
            "info": "chat1_info",
            "user_id": 1,
            "members": [1, 3]
        },
        {
            "id": 2,
            "title": "chat2",
            "info": "chat2_info",
            "user_id": 2,
            "members": [2, 3]
        },
        {
            "id": 3,
            "title": "chat3",
            "info": "chat3_info",
            "user_id": 3,
            "members": [3, ]
        },
    ]
    messages = [
        {
            "id": 1,
            "user_id": 1,
            "chat_id": 1,
            "text": "message_1",
            "created_at": "20.03.2022 21:33"
        },
        {
            "id": 2,
            "user_id": 2,
            "chat_id": 2,
            "text": "message_2",
            "created_at": "20.03.2022 21:33"
        },
        {
            "id": 3,
            "user_id": 3,
            "chat_id": 3,
            "text": "message_3",
            "created_at": "20.03.2022 21:33"
        }
    ]


# pprint(Storage.chats)
