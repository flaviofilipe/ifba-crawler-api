from src.contexts.shared.domain.usecase import UseCase


class GetPostsUseCaseSpy(UseCase):
    def __int__(self):
        ...

    def execute(self, **kwargs):
        return 'test'
