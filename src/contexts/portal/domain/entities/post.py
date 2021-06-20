from datetime import date


class Post:
    def __init__(self, title: str, link: str, created_at: date) -> None:
        self.title = title
        self.link = link
        self.created_at = created_at

    def __str__(self) -> str:
        return self.title
