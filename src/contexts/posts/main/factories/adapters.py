from src.contexts.posts.infra.adapters.db.mongo_repository import MongoDB


def make_mongo_repository():
    return MongoDB()
