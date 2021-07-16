from src.contexts.posts.data.ports.db import Database
from src.contexts.posts.domain.entities import Post
from src.contexts.posts.domain.usecases import PostTypeParams
from src.contexts.shared.domain.usecase import UseCase


class CreatePostUsecase(UseCase):

    def __init__(self, db: Database):
        self.db = db

    def execute(self, params: PostTypeParams) -> Post:
        return self.db.create_post(params)
