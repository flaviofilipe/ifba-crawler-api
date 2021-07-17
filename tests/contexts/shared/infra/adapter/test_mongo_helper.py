from pymongo import MongoClient
from pymongo.database import Database

from src.contexts.shared.infra.adapters.mongo_helper import connection, client


def test_connection_is_a_database_instance():
    assert isinstance(connection, Database)


def test_client_is_a_mongo_client_instance():
    assert isinstance(client, MongoClient)
