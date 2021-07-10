from src.contexts.integration.ifba.data.usecases import GetPostsUsecase
from src.contexts.integration.ifba.main.factories.services.http_port_service import make_http_adapter


def make_get_posts_usecase():
    return GetPostsUsecase(make_http_adapter())
