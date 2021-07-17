import json
from typing import Callable

from pymongo import MongoClient

from src.contexts.posts.data.ports.db import Database
from src.contexts.posts.domain.entities import Post
from src.contexts.posts.domain.usecases import PostTypeParams


class MongoDB(Database):

    def __init__(self, db_cli: MongoClient):
        self.db_cli = db_cli

    def create_post(self, params: PostTypeParams) -> Post:
        post = Post(params['title'], params['link'], params['created_at'])
        return self.db_cli['posts'].insert_one(post.__dict__())
