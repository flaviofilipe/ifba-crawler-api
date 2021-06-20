from datetime import date
import typing


class NewsTypeParams(typing.TypedDict):
    title: str
    link: str
    created_at: date