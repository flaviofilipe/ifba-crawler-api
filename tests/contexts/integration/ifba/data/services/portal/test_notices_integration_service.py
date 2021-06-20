import pytest
from src.contexts.integration.ifba.data.services.portal.notices_integration_service import \
    PostsIntegrationService
from tests.contexts.portal.mocks.ports import HttpPortSpy


@pytest.fixture
def notices_integration_service():
    http_port = HttpPortSpy()
    return PostsIntegrationService(http_port)


def test_get_array_posts(notices_integration_service):
    posts = notices_integration_service.get_posts()
    assert len(posts) > 0
