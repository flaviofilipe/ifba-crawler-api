from src.contexts.integration.ifba.data.ports.client.http_port import HttpPort

url = 'https://portal.ifba.edu.br/conquista/noticias-2/noticias-campus-vitoria-da-conquista'


def get_posts(http_port: HttpPort, start=1) -> list:
    b_start = 0 if start == 1 else 30 * (start - 1)
    page_url = '{}?b_start:int={}'.format(url, b_start)
    posts = http_port.get_posts(page_url, verify=False)
    return posts

