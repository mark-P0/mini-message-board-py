"""
https://jinja.palletsprojects.com/en/stable/api/#basics
"""

import typing as T

from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader("./templates/html"), autoescape=select_autoescape()
)


def render_template(template_name: str, **kwargs: T.Any):
    template = env.get_template(template_name)
    rendered = template.render(**kwargs)

    return rendered
