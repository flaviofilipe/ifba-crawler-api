from datetime import date
import typing


class PostTypeParams(typing.TypedDict):
    title: str
    link: str
    created_at: date
