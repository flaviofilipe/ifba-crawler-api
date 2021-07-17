from src.contexts.posts.data.ports.db import Database
from src.contexts.posts.domain.entities import Post
from src.contexts.posts.domain.usecases import PostTypeParams
from src.contexts.posts.main.factories.controllers import make_get_posts_controller
from src.contexts.posts.main.factories.usecases import make_post_usecase
from tests.mocks.posts import mock_post, mock_params


class MongoDBSpy(Database):

    def create_post(self, params: PostTypeParams) -> Post:
        return mock_post(params)


def test_make_get_posts_controller():
    params = mock_params()
    mongo_repository_spy = MongoDBSpy()
    posts_usecase = make_post_usecase(mongo_repository_spy)
    controller = make_get_posts_controller(params, posts_usecase)
    assert controller.title == params['title']
