import datetime
from uuid import uuid4

from pydantic import BaseModel


class Message(BaseModel):
    id: str
    user: str
    text: str
    added: datetime.datetime

    @classmethod
    def get_all(cls):
        return _messages

    @classmethod
    def get_one(cls, message_id: str, /):
        for message in _messages:
            if message.id == message_id:
                return message

        return None

    @classmethod
    def add_one(cls, *, user: str, text: str):
        message = Message(
            id=str(uuid4()),
            user=user,
            text=text,
            added=datetime.datetime.now(),
        )

        _messages.append(message)


_messages: list[Message] = [
    Message(
        id=str(uuid4()),
        user="Amando",
        text="Hi there!",
        added=datetime.datetime.now(),
    ),
    Message(
        id=str(uuid4()),
        user="Charles",
        text="Hello World!",
        added=datetime.datetime.now(),
    ),
]
"""
```
const messages = {
    text: "Hi there!",
    user: "Amando",
    added: new Date()
  },
  {
    text: "Hello World!",
    user: "Charles",
    added: new Date()
  }
```
"""
