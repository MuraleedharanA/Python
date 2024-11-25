from pymongo.mongo_client import MongoClient
import pandas as pd
from bson.objectid import ObjectId
uri="mongodb+srv://rohithrajreganti:rohithrajreganti@cluster0.rd7dn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient(uri,tlsAllowInvalidCertificates=True)
    print("success")

    db=client['ust_live_quiz']

    collection=db['basic_collection_test']

    #docId= '67383a8cdef166f424f1d4eb'
    query = {"Name": "Athira M"}
    

    results = collection.find(query)
except Exception as e:
    print(e)

result_list = list(results)

df = pd.DataFrame(result_list)
print(df.head())
print(df.columns)
df.to_csv("mongoDEmo.csv")
