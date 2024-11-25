from pymongo.mongo_client import MongoClient
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json



"""Get data from Mongodb and convert to DF"""
uri="mongodb+srv://athiraMuraleedharan:Beta$1234566@cluster0.a3wjc.mongodb.net"

try:
        client = MongoClient(uri,tlsAllowInvalidCertificates=True)
        print("success")

        db=client['sample_mflix']

        collection=db['movies']

        results = collection.find()
        #print(results)
        
except Exception as e:
        print(e)

resultList = list(results)

df=pd.DataFrame(resultList)

#df.set_index('_id',inplace=True)
df.to_csv("sample.csv")

print(df.head())
print(df.columns)



DATABASE_URL = 'sqlite:///Movies.db'
engine = create_engine(DATABASE_URL,echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)


#Create the DB
Base.metadata.create_all(engine)
"""writes the DF to sql"""
#engine = create_engine("sqlite:///movies.db",echo=True)
df.to_sql(name='MoviesTable',con=engine,if_exists='replace',index=False)



