from src.contexts.integration.ifba.infra.adapters.client.http_adapter import HttpAdapter, HttpPort


def make_http_adapter() -> HttpPort:
    return HttpAdapter()
