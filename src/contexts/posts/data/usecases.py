from src.contexts.posts.domain.entities import Post
from src.contexts.posts.domain.usecases import NewsTypeParams
from src.contexts.posts.data.ports.db_port import PostRepository
from src.contexts.shared.domain.usecase import UseCase


class CreatePostUsecase(UseCase):

    def __init__(self, posts_repository: PostRepository):
        self.posts_repository = posts_repository

    def execute(self, params: NewsTypeParams) -> Post:
        posts_repository = self.posts_repository
        return posts_repository.create_post(params)
