import pytest
from src.contexts.portal.data.usecases.creat_posts_usecase import CreatePostsUseCase


@pytest.fixture
def post():
    return CreatePostsUseCase()

def test_should_create_new_post(post):
    print('Aqui')
    assert post