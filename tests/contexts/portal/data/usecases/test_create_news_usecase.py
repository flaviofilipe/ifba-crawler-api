import pytest
from datetime import date
from src.contexts.portal.data.usecases.creat_posts_usecase import CreatePostsUseCase
from src.contexts.portal.domain.usecases.create_post import NewsTypeParams


@pytest.fixture
def post():
    return CreatePostsUseCase()


def test_should_create_new_post(post):
    params: NewsTypeParams = {
        'title': 'Teste',
        'link': '',
        'date': date.today()
    }

    post = post.execute(params)
    assert post.title == params['title']
