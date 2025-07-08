from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


# user table
class UserModel(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    age = Column(Integer)


# group table
class GroupModel(Base):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
