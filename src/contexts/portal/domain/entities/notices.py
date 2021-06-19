from datetime import date

class Notices:
    def __init__(self, title: str, link: str, date: date) -> None:
        print(date.year)
        self.title = title
        self.link = link
        self.date = date

    def __str__(self) -> str:
        return self.title
