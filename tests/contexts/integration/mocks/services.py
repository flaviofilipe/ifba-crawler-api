from src.contexts.integration.ifba.data.ports.client.http_port import HttpPort
from tests.mocks.posts import mock_post


class HttpPortSpy(HttpPort):

    def get_posts(self, page_url: str, verify: bool) -> list:
        return [mock_post]
