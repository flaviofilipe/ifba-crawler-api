from ...ports.client.http_port import HttpPort


class PostsIntegrationService:
    def __init__(self, http_port: HttpPort) -> None:
        self.http_port = http_port
        self.url = 'https://portal.ifba.edu.br/conquista/noticias-2/noticias-campus-vitoria-da-conquista'

    def get_posts(self, start=1) -> list:
        b_start = 0 if start == 1 else 30 * (start - 1)
        page_url = '{}?b_start:int={}'.format(self.url, b_start)
        posts = self.http_port.get_posts(page_url, verify=False)
        return posts
