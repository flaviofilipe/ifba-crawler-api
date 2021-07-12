from src.contexts.integration.ifba.data.usecases import GetPostsUsecase
from src.contexts.integration.ifba.main.factories.services import make_http_adapter, make_get_posts_service


def make_get_posts_usecase():
    return GetPostsUsecase(make_http_adapter(), make_get_posts_service())
