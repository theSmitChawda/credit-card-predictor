import predictor
import mongo_cloud_connection_str

import time
from pymongo import MongoClient

# Connecting to MongoDB

client = MongoClient(mongo_cloud_connection_str.CONNECTION_STRING)
db = client.test
print('\n\nLOG: Connection Tested...\n\n')

db = client[mongo_cloud_connection_str.DB_NAME]
print('\n\nLOG: Connected to database...\n\n')

collection = db[mongo_cloud_connection_str.COLLECTION_NAME]
print('\n\nLOG: Collection located...\n\n')

one_record = None

while one_record == None:
    print('LOG: Blank document')
    one_record = collection.find_one()
    time.sleep(5)
else:
    print('LOG: Document Found')
    # TODO: Document parsing logic goes here
    