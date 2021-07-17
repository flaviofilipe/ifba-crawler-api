from datetime import date


class Post:
    def __init__(self, title: str, link: str, created_at: date) -> None:
        self._id = ''
        self.title = title
        self.link = link
        self.created_at = created_at

    def __str__(self) -> str:
        return self.title

    def __dict__(self) -> dict:
        return {
            'title': self.title,
            'link': self.link,
            'created_at': self.created_at.__str__()
        }
