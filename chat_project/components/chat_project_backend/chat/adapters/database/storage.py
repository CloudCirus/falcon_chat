from pprint import pprint


class Storage:
    users = [
        {
            "id": 1,
            "username": "user1",
            "auth": None
        },
        {
            "id": 2,
            "username": "user2",
            "auth": None,
        },
        {
            "id": 3,
            "username": "user3",
            "auth": None,
        }
    ]
    chats = [
        {
            "id": 1,
            "title": "chat1",
            "info": "chat1_info",
            "owner": 1,
            "members": [1, 2, 3]
        },
        {
            "id": 2,
            "title": "chat2",
            "info": "chat2_info",
            "owner": 2,
            "members": [2, 3]
        },
        {
            "id": 3,
            "title": "chat3",
            "info": "chat3_info",
            "owner": 3,
            "members": [3, ]
        },
    ]
    messages = [
        {
            "id": 1,
            "user_id": 1,
            "chat_id": 1,
            "text": "message_1",
        },
        {
            "id": 2,
            "user_id": 2,
            "chat_id": 2,
            "text": "message_2",
        },
        {
            "id": 3,
            "user_id": 3,
            "chat_id": 3,
            "text": "message_3",
        }
    ]


pprint(Storage.chats)
