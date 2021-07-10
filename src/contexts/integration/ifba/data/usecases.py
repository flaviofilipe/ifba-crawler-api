from src.contexts.integration.ifba.data.ports.client.http_port import HttpPort
from src.contexts.integration.ifba.data.services.portal_integration_service import get_posts
from src.contexts.shared.domain.usecase import UseCase


class GetPostsUsecase(UseCase):
    def __init__(self, http_port: HttpPort):
        self.http_port = http_port

    def execute(self, start=1) -> list:
        return get_posts(self.http_port, start)
