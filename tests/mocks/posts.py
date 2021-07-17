from datetime import date
from faker import Faker
from faker.providers import internet
from src.contexts.posts.domain.entities import Post
from src.contexts.posts.domain.usecases import PostTypeParams

faker = Faker()
providers = internet.Provider(faker)


def mock_params() -> PostTypeParams:
    params: PostTypeParams = {
        'title': faker.sentence(),
        'link': providers.safe_domain_name(),
        'created_at': date.today()
    }
    return params


def mock_post(params: PostTypeParams = None) -> Post:
    if params is None:
        params = mock_params()
    return Post(params['title'], params['link'], params['created_at'])
