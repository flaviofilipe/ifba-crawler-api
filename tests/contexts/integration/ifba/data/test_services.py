from src.contexts.integration.ifba.data.services.portal_integration_service import get_posts
from tests.contexts.posts.mocks.ports import HttpPortSpy


def test_get_array_posts():
    http_port = HttpPortSpy()
    posts = get_posts(http_port)
    assert len(posts) > 0
