import datetime

from pydantic import BaseModel


class Message(BaseModel):
    user: str
    text: str
    added: datetime.datetime


messages: list[Message] = [
    Message(user="Amando", text="Hi there!", added=datetime.datetime.now()),
    Message(user="Charles", text="Hello World!", added=datetime.datetime.now()),
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
