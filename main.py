import predictor
import mongo_cloud_connection_str
from pymongo import MongoClient

client = MongoClient(mongo_cloud_connection_str.CONNECTION_STRING)
db = client.test
print('\n\nLOG: Connection Tested...\n\n')

db = client[mongo_cloud_connection_str.DB_NAME]
print('\n\nLOG: Connected to database...\n\n')

collection = db[mongo_cloud_connection_str.COLLECTION_NAME]
print('\n\nLOG: Collection located...\n\n')