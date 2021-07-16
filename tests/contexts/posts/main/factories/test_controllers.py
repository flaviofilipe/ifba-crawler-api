from src.contexts.posts.main.factories.controllers import make_get_posts_controller
from src.contexts.posts.main.factories.usecases import make_post_usecase
from src.contexts.posts.main.factories.adapters import make_mongo_repository
from tests.contexts.posts.mocks.posts import make_params


def test_make_get_posts_controller():
    params = make_params()
    mongo_repository = make_mongo_repository()
    posts_usecase = make_post_usecase(mongo_repository)
    controller = make_get_posts_controller(params, posts_usecase)
    assert controller.title == params['title']
