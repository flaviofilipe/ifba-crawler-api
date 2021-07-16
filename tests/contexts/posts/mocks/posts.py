from datetime import date
from faker import Faker
from faker.providers import internet
from src.contexts.posts.domain.usecases import PostTypeParams

faker = Faker()
providers = internet.Provider(faker)


def make_params() -> PostTypeParams:
    params: PostTypeParams = {
        'title': faker.sentence(),
        'link': providers.safe_domain_name(),
        'created_at': date.today()
    }
    return params
