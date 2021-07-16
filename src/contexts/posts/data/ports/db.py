from src.contexts.posts.domain.entities import Post
from abc import ABC, abstractmethod

from src.contexts.posts.domain.usecases import PostTypeParams


class Database(ABC):
    @abstractmethod
    def create_post(self, params: PostTypeParams) -> Post:
        pass
