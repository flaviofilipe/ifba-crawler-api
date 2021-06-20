from abc import ABC, abstractmethod
from src.contexts.portal.domain.usecases.create_post import NewsTypeParams
from src.contexts.portal.domain.entities.post import Post


class PostRepository(ABC):
    @abstractmethod
    def create_post(self, params: NewsTypeParams) -> Post:
        ...
