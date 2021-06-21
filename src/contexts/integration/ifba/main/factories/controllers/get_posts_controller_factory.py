from src.contexts.integration.ifba.presentation.controllers.get_posts_controller import GetPostsController
from src.contexts.integration.ifba.main.factories.usecases.get_posts_usecase_factory import make_get_posts_usecase


def make_get_posts_controller():
    return GetPostsController(make_get_posts_usecase())
