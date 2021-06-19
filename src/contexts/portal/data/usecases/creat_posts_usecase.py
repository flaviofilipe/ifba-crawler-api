from src.contexts.shared.domain.usecases.usecase import UseCase
from src.contexts.portal.domain.entities.posts import Posts
from src.contexts.portal.domain.usecases.create_post import NewsTypeParams


class CreatePostsUseCase(UseCase):
    def __init__(self) -> None:
        ...

    def execute(self, news: NewsTypeParams) -> Posts:
        return Posts(news['title'], news['link'], news['date'])
