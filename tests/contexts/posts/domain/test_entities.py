import json
import pytest
from datetime import date, datetime

from bson import json_util
from faker import Faker
from faker.providers import internet
from src.contexts.posts.domain.entities import Post

faker = Faker()

providers = internet.Provider(faker)

now = date.today()
title = faker.sentence()
link = providers.safe_domain_name()


@pytest.fixture
def new_post():
    return Post(title, link, now)


def test_create_notice(new_post):
    assert new_post.title == title


def test_get_date(new_post):
    assert new_post.created_at.isoformat() == now.isoformat()


def test_get_link(new_post):
    assert new_post.link == link


def test_get_dict(new_post):
    assert isinstance(new_post.__dict__(), dict)
