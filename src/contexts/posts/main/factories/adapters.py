from src.contexts.posts.infra.adapters.db.mongo_repository import MongoDB
from src.contexts.shared.infra.adapters.mongo_helper import connection


def make_mongo_repository():
    return MongoDB(connection)
