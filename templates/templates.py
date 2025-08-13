"""
https://jinja.palletsprojects.com/en/stable/api/#basics
"""

import typing as T

from jinja2 import Environment, FileSystemLoader, select_autoescape

from messages import Message

env_loader = FileSystemLoader("./templates/html")
env = Environment(loader=env_loader, autoescape=select_autoescape())


class IndexTemplate:
    name = "index.html"

    class Context(T.TypedDict):
        title: str
        messages: list[Message]

    @classmethod
    def render(cls, **kwargs: T.Unpack[Context]):
        template = env.get_template(cls.name)
        rendered = template.render(**kwargs)

        return rendered
