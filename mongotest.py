import pymongo


##client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
##db = client.test
##print(db)

client = pymongo.MongoClient("mongodb+srv://bharadwaz:Omsairam123@clusterineuron.oafgb5f.mongodb.net/?retryWrites=true&w=majority")
db1 = client.test
print(db1)

d = {
    "name" : "Bharadwaz",
    "email" : "Bharadwaz@gmail.com",
    "surname": "kumar"
}

db2 = client['mongotest']
coll =db2['test']
coll.insert_one(d )