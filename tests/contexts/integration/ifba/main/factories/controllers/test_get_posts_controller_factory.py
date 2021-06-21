from src.contexts.integration.ifba.main.factories.controllers.get_posts_controller_factory import \
    make_get_posts_controller


def test_create_controller_factory_and_return_posts_from_portal():
    controller = make_get_posts_controller().handler()
    assert controller
