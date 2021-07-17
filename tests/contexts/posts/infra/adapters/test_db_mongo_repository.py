import mongomock
from bson import ObjectId
from src.contexts.posts.infra.adapters.db.mongo_repository import MongoDB
from tests.mocks.posts import mock_params


def test_should_instert_new_post_in_mongodb():
    params = mock_params()
    con = mongomock.MongoClient()['posts']
    mongo = MongoDB(con)
    post = mongo.create_post(params)
    assert isinstance(post.inserted_id, ObjectId)
