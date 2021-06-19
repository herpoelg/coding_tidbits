#basic crud (create, read, update and delete) operations with pymongo, a library for mongoDB

#pymongo documentation: https://pypi.org/project/pymongo/

from pymongo import MongoClient

#connecting
client = MongoClient("mongodb+srv://m001-student:m001-mongodb-basics@sandbox.h81wz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

test_db = client.data
collection = test_db.test_coll

#cleaning previous data:
collection.delete_many({})

#create: insert one
test_dic = {'name': 'Glenn', 'salary': 1205,'department': 'Data Integration'}
inserted = collection.insert_one(test_dic)
print('Docment inserted at: ', inserted.inserted_id.generation_time)

#create: insert many via an array of documents
many_ldic = [
     { 'name': 'Goran', 'salary': 4500},
     { 'name': 'Jordy', 'salary': 4500},
     { 'name': 'Matiz', 'salary': 5000, 'department': 'Reparations', 'hasCompanyCar': True}
   ]
inserted_many = collection.insert_many(many_ldic)
print("Object returned after executing insert_many", inserted_many) #prints a pymongo.results.InsertManyResult object


#read: via the find function
res = collection.find()
print("result of .find():", res) # returns a cursor which allows you to iterate over all matching documents

#loop over the cursor (max 2 times):
i = 0
for doc in res:
    print(doc)
    i +=1
    if i > 1:
        break


#read: via the find_one function
res_one = collection.find_one() #returns a document
print("result of find one without argument:", res_one)

#querying the collection with exact input
find_goran = {"name": "Goran"}
res_goran = collection.find(find_goran)
print(res_goran)#returns a cursor which allows you to iterate over all matching documents

#loop over the cursor (max 2 times):
i = 0
for doc in res_goran:
    print(doc)
    i +=1
    if i > 1:
        break


res_goran = collection.find_one(find_goran)
print(res_goran)

find_ruben = {"name": "Ruben"}
res_ruben = collection.find_one(find_ruben)
if res_ruben is None:
    print(find_ruben['name'], 'is not in the collection.')
else:
    print(res_ruben)

#update via: update_one(), update_many(), replace_one()

# The general syntax for all the above methods is
# <method_name>(condition, update_or_replace_document, upsert=False, bypass_document_validation=False)
# Here
# condition: A query that matches the document to replace.
# update_or_replace_document: The new document.
# upsert (optional): If True, perform an insert if no documents match the filter.
# bypass_document_validation: (optional) If True, allows the write to opt-out of document level validation. Default is False.
# Following are the snippets forh update(), update_one(), update_many() and replace_one(). All the methods will return UpdateResult object except update().
#update_one
upd1 = collection.update_one({"name": "Glenn"}, {"$set": {"name": "Goran"}})
print("Update_one:", upd1)

#update_many
updmany = collection.update_many({"name": "Goran"}, {"$set": {"name": "Eric"}})
print(updmany)

#replace_one
repl1 = collection.replace_one({"name":"Friedel"}, {"name":"Frida"})
print(repl1)


#delete:# delete_one, delete_many
del1 = collection.delete_one({"name": "Matix"})
print(del1)

delmany = collection.delete_many({"name": "Goran"})
print(delmany)


