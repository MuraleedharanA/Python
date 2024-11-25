from pymongo.mongo_client import MongoClient
import pandas as pd
uri="mongodb+srv://rohithrajreganti:rohithrajreganti@cluster0.rd7dn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient(uri,tlsAllowInvalidCertificates=True)
    print("success")

    db=client['sample_mflix']

    collection=db['movies']

    results = collection.find().limit(5)
    
except Exception as e:
    print(e)

#finally:
   # client.close()

result_list = list(results)

df = pd.DataFrame(result_list)
print(df.head())
print(df.columns)