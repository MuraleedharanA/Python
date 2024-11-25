from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#define the DB
DATABASE_URL = 'sqlite:///Movies.db'
engine = create_engine(DATABASE_URL,echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

#define ORM Model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(String, nullable = False)
    age = Column(Integer,nullable=False)

#Create the DB and tables
Base.metadata.create_all(engine)

#create new session
session = SessionLocal()

#create
#new_user = User(name="Akshay",age=99)
#session.add(new_user)
#session.commit()

#read
users = session.query(User).all()
print(users)
for user in users:
    print(user.id,user.name,user.age)

#update
user_to_update = session.query(User).filter_by(name='Athira').first()
if(user_to_update):
    user_to_update.age = 32
    session.commit()

#del
user_to_update = session.query(User).filter_by(name='Athira').first()
if(user_to_update):
    session.delete(user_to_update)
    session.commit()


session.close()