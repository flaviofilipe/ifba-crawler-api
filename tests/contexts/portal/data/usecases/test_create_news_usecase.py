import pytest
from src.contexts.posts.data.usecases.creat_posts_usecase import CreatePostsUseCase
from tests.contexts.portal.mocks.repositories import PostRepositorySpy, make_params

params = make_params()


@pytest.fixture
def post():
    post_repository_spy = PostRepositorySpy(params)
    return CreatePostsUseCase(post_repository_spy)


def test_should_create_new_post(post):
    post = post.execute(params)
    assert post.title == params['title']
    assert post.link == params['link']
    assert post.created_at == params['created_at']
