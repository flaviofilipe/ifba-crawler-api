from typing import Callable

from src.contexts.integration.ifba.data.ports.client.http_port import HttpPort
from src.contexts.shared.domain.usecase import UseCase


class GetPostsUsecase(UseCase):
    def __init__(self, http_port: HttpPort, get_posts_service: Callable):
        self.http_port = http_port
        self.get_posts_service = get_posts_service

    def execute(self, start=1) -> list:
        return self.get_posts_service(self.http_port, start)
