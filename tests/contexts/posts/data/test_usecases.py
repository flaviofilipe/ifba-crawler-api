import pytest
from src.contexts.posts.data.usecases import CreatePostUsecase
from tests.contexts.posts.mocks.repositories import PostRepositorySpy, make_params

params = make_params()


@pytest.fixture
def post():
    return PostRepositorySpy(params)


def test_should_create_new_post(post):
    create_post_usecase = CreatePostUsecase(post)
    post = create_post_usecase.execute(params)
    assert post.title == params['title']
    assert post.link == params['link']
    assert post.created_at == params['created_at']
