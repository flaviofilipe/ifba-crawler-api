from src.contexts.shared.domain.usecases.usecase import UseCase
from src.contexts.portal.domain.entities.post import Post
from src.contexts.portal.domain.usecases.create_post import NewsTypeParams
from ..ports.db.posts_repository import PostRepository


class CreatePostsUseCase(UseCase):
    def __init__(self, posts_repository: PostRepository) -> None:
        self.posts_repository = posts_repository

    def execute(self, params: NewsTypeParams) -> Post:
        return self.posts_repository.create_post(params)
