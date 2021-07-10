from datetime import date
from faker import Faker
from faker.providers import internet
from src.contexts.posts.domain.entities import Post

faker = Faker()


def mock_post() -> Post:
    params = {
        'title': faker.sentence(),
        'link': internet.Provider.safe_domain_name,
        'date': date.today()
    }

    return Post(params['title'], params['link'], params['date'])
