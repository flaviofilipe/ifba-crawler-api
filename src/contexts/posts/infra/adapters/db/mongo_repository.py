from src.contexts.posts.data.ports.db import Database
from src.contexts.posts.domain.entities import Post
from src.contexts.posts.domain.usecases import PostTypeParams


class MongoDB(Database):
    def create_post(self, params: PostTypeParams) -> Post:
        post = Post(params['title'], params['link'], params['created_at'])
        return post

