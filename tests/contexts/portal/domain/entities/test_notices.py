import faker
import pytest
from datetime import date
from faker import Faker
from faker.providers import internet
from src.contexts.portal.domain.entities.notices import Notices

faker = Faker()
now = date.today()
title = faker.sentence()
link = internet.Provider.safe_domain_name

@pytest.fixture
def new_notice():
    return Notices(title, link,  now)

def test_create_notice(new_notice):
    assert new_notice.title == title

def test_get_date(new_notice):
    assert new_notice.date.isoformat() == now.isoformat()

def test_get_link(new_notice):
    assert new_notice.link == link