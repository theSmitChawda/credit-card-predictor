import predictor
import mongo_cloud_connection_str
from pymongo import MongoClient

client = MongoClient(mongo_cloud_connection_str.CONNECTION_STRING)
db = client.test
