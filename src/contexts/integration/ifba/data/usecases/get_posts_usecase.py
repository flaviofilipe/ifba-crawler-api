from src.contexts.shared.domain.usecases.usecase import UseCase
from src.contexts.integration.ifba.data.ports.client.http_port import HttpPort


class GetPostUseCase(UseCase):
    def __init__(self, ifba_service: HttpPort):
        self.ifba_service = ifba_service

    def execute(self, start=1):
        b_start = 0 if start == 1 else 30 * (start - 1)
        url = 'https://portal.ifba.edu.br/conquista/noticias-2/noticias-campus-vitoria-da-conquista'
        page_url = f'{url}?b_start:int={b_start}'
        return self.ifba_service.get_posts(page_url, False)
