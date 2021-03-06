

from src.contexts.posts.data.ports.db import Database
from src.contexts.posts.domain.entities import Post
from src.contexts.posts.domain.usecases import PostTypeParams
from tests.mocks.posts import mock_params


class PostRepositorySpy(Database):
    def __init__(self, params):
        self.params = params if params else mock_params()

    def create_post(self, params: PostTypeParams):
        return Post(self.params['title'], self.params['link'], self.params['created_at'])
