import pytest
from unittest import mock
from ....mocks.usecases import GetPostsUseCaseSpy
from src.contexts.integration.ifba.presentation.controllers.get_posts_controller import GetPostsController


@mock.patch.object(GetPostsUseCaseSpy, 'execute')
def test_should_create_controller(mock_usecase):
    usecase = GetPostsUseCaseSpy()
    controller = GetPostsController(usecase)
    controller.handler()
    mock_usecase.assert_called_once()
