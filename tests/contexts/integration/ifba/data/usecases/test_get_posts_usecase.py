from src.contexts.integration.ifba.data.usecases.get_posts_usecase import GetPostUseCase
from ....mocks.services import HttpPortSpy


def test_should_call_get_post_method():
    http_port = HttpPortSpy()
    response = GetPostUseCase(http_port).execute()
    assert len(response) > 0
