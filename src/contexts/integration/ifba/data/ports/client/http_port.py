from abc import ABC, abstractmethod


class HttpPort(ABC):
    @abstractmethod
    def get_posts(self, page_url: str, verify: bool) -> list:
        ...
