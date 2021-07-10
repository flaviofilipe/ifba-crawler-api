from abc import ABC, abstractmethod
from src.contexts.posts.domain.usecases import NewsTypeParams
from src.contexts.posts.domain.entities import Post


class PostRepository(ABC):
    @abstractmethod
    def create_post(self, params: NewsTypeParams) -> Post:
        ...
