from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Date


engine = create_engine('mysql+mysqlconnector://'':password @localhost[:3306]/<slangs>')
Session = sessionmaker(bind=engine)

Base = declarative_base()

class slangs(Base):
    __tablename__:"slangs"
    id = Column(Integer, primary_key = True)
    word = Column(String)
    meaning = Column(String)

    def __init__(self , word , meaning):
        self.word = word
        self.meaning = meaning
    
    def __repr___(self):
        return f"{self.word} suele significar {self.meaning}"

