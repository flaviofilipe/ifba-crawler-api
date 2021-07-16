from src.contexts.posts.domain.entities import Post
from src.contexts.shared.domain.usecase import UseCase
from src.contexts.posts.domain.usecases import PostTypeParams


class CreatePostsController:
    def __init__(self, create_posts_usecase: UseCase):
        self.create_posts_usecase = create_posts_usecase

    def handler(self, params: PostTypeParams) -> Post:
        posts = self.create_posts_usecase.execute(params)
        return posts
