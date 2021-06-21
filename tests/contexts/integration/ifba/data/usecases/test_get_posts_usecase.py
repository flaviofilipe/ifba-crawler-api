from unittest import mock
from src.contexts.integration.ifba.data.usecases.get_posts_usecase import GetPostUseCase
from ....mocks.services import HttpPortSpy


@mock.patch.object(HttpPortSpy, 'get_posts')
def test_should_call_get_post_method(http_port_mock):
    http_port = HttpPortSpy()
    get_post_use_case = GetPostUseCase(http_port)
    get_post_use_case.execute()
    http_port_mock.assert_called_once()
