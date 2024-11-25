from pymongo.mongo_client import MongoClient
import pandas as pd
from bson.objectid import ObjectId
uri="mongodb+srv://rohithrajreganti:rohithrajreganti@cluster0.rd7dn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient(uri,tlsAllowInvalidCertificates=True)
    print("success")

    db=client['ust_live_quiz']

    collection=db['basic_collection_test']

    docId= '67383a8cdef166f424f1d4eb'
    query = {"_id": ObjectId(docId)}
    

    update={"$set" :{"name":"Athira Muraleedharan",
                     "age":"100",
                     "city":"COK"}}
    result = collection.update_one(query,update)
    if(result.matched_count>0):
        print("updated")
    
except Exception as e:
    print(e)
