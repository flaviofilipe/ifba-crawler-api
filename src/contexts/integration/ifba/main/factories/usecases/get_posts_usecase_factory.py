from src.contexts.integration.ifba.data.usecases.get_posts_usecase import GetPostUseCase, UseCase
from src.contexts.integration.ifba.main.factories.services.http_port_service import make_http_adapter


def make_get_posts_usecase() -> UseCase:
    return GetPostUseCase(make_http_adapter())
