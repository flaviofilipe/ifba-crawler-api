from src.contexts.posts.data.usecases import CreatePostUsecase
from src.contexts.posts.data.ports.db import Database


def make_post_usecase(db: Database):
    return CreatePostUsecase(db)
