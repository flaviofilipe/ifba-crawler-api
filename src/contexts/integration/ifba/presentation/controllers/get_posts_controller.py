from src.contexts.shared.presentation.protocols.controller import Controller
from src.contexts.shared.domain.usecases.usecase import UseCase


class GetPostsController(Controller):
    def __init__(self, create_post_usecase: UseCase):
        self.create_post_usecase = create_post_usecase

    def handler(self, page: int = 1):
        return self.create_post_usecase.execute(page)
