#basic crud operations with pymongo

from pymongo import MongoClient

#connecting
client = MongoClient('localhost',27017)  # 27017 is the default port number for mongodb

db = client.test
col = db.person

#creating

col.insert_one({'x': 1})

db.test.count_documents({'x': 1})

result = db.test.insert_one({'x': 1})
result.inserted_id

db.test.find_one({'x': 1})
