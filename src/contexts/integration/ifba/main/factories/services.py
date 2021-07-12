from typing import Callable

from src.contexts.integration.ifba.data.services.portal_integration_service import get_posts
from src.contexts.integration.ifba.infra.adapters.client.http_adapter import HttpAdapter, HttpPort


def make_http_adapter() -> HttpPort:
    return HttpAdapter()


def make_get_posts_service() -> Callable:
    return get_posts
