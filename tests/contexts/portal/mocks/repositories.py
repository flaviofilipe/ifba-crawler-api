from datetime import date
from faker import Faker
from faker.providers import internet

from src.contexts.posts.data.ports.db_port import PostRepository
from src.contexts.posts.domain.entities import Post
from src.contexts.posts.domain.usecases import NewsTypeParams

faker = Faker()
providers = internet.Provider(faker)


def make_params() -> NewsTypeParams:
    params: NewsTypeParams = {
        'title': faker.sentence(),
        'link': providers.safe_domain_name(),
        'created_at': date.today()
    }
    return params


class PostRepositorySpy(PostRepository):
    def __init__(self, params):
        self.params = params if params else make_params()

    def create_post(self, params: NewsTypeParams):
        return Post(self.params['title'], self.params['link'], self.params['created_at'])
