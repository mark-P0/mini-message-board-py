import datetime
from uuid import uuid4

from pydantic import BaseModel


class Message(BaseModel):
    id: str
    user: str
    text: str
    added: datetime.datetime


messages: list[Message] = [
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


def add_message(*, user: str, text: str):
    messages.append(
        Message(
            id=str(uuid4()),
            user=user,
            text=text,
            added=datetime.datetime.now(),
        )
    )


def get_message(message_id: str, /):
    for message in messages:
        if message.id == message_id:
            return message

    return None
