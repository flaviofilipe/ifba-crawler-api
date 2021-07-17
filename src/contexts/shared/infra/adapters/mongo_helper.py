import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

host = os.getenv("MONGO_HOST")
port = int(os.getenv("MONGO_PORT"))
database = os.getenv("MONGO_DATABASE")


client = MongoClient(host, port)
connection = client[database]
