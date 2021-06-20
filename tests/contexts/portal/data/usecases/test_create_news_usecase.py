import pytest
from datetime import date
from src.contexts.portal.data.usecases.creat_posts_usecase import CreatePostsUseCase
from src.contexts.portal.domain.usecases.create_post import NewsTypeParams
from src.contexts.portal.data.ports.db.posts_repository import PostRepository
from src.contexts.portal.domain.entities.post import Post


class PostRepositorySpy(PostRepository):
    def create_post(self, params: NewsTypeParams):
        return Post('Teste', '', date.today())


@pytest.fixture
def post():
    post_repository_spy = PostRepositorySpy()
    return CreatePostsUseCase(post_repository_spy)


def test_should_create_new_post(post):
    params: NewsTypeParams = {
        'title': 'Teste',
        'link': '',
        'created_at': date.today()
    }

    post = post.execute(params)
    assert post.title == params['title']
    assert post.link == params['link']
    assert post.created_at == params['created_at']
