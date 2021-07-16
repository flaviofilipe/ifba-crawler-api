from src.contexts.posts.domain.usecases import PostTypeParams
from src.contexts.posts.presentation.controllers import CreatePostsController
from src.contexts.shared.domain.usecase import UseCase


def make_get_posts_controller(params: PostTypeParams, post_usecase: UseCase):
    return CreatePostsController(post_usecase).handler(params)
