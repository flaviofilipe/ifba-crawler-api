import pytest
from src.contexts.integration.ifba.infra.adapters.client.http_adapter import HttpAdapter

url = 'https://portal.ifba.edu.br/conquista/noticias-2/noticias-campus-vitoria-da-conquista'
page_url = '{}?b_start:int={}'.format(url, 0)


@pytest.fixture
def get_posts_fixture():
    http_adapter = HttpAdapter()
    return http_adapter.get_posts(page_url, verify=False)


def test_should_return_30_post_from_portal(get_posts_fixture):
    assert len(get_posts_fixture) == 30


def test_it_should_have_title_link_and_date(get_posts_fixture):
    assert get_posts_fixture[0]['title']
    assert get_posts_fixture[0]['link']
    assert get_posts_fixture[0]['date']
