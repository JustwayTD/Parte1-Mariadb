import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Date

engine = create_engine('mysql+mysqlconnector://'':password @localhost[:3306]/<slangs>')
Session = sessionmaker(bind=engine)
session = Session()
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

c = session.query(slangs)

def agregar(word1,palabraS):
    """Adds a new word to our data base"""
    word1 = word1.strip()
    palabraS = palabraS.strip()
    new_word = slangs(word = word1 , meaning = palabraS)
    c.session.add(new_word)
    c.session.commit()
    print("Cool! La palabra ",word1,"ha sido añadida")
def menu():
    """Menú principal del programa """
    opc = int(input("Bienvenido Fren! ¿Que vamos a hacer hoy?\n1) Agregar nueva palabra \n2) Editar palabra existente \n3) Eliminar alguna palabra existente \n4) Ver listado de palabras \n5) Buscar significado de palabra \n6) Salir\n"))
    return opc
def editaMoh(wordto,newmean):
    """Edits an already existing word from our database"""
    wordto.strip()
    newmean.strip()
    search_word = slangs.query.filter_by(word = wordto).first
    search_word.definition = newmean
    c.session.commit()

def eliminaMoh (word_todel):
    """Deletes certain word from our database"""
    del_wor= slangs.query.filter_by(word = word_todel).first
    c.session.delete(del_wor)
    c.session.commit()

def urbanDic():
    """Shows all elements from my database slangs"""
    words = slangs.query.all()
    return words
def whatIsLove(babyDont):
    """Shows a Description of a certain word"""
    babyDont.strip()
    print("la palabra es:", babyDont)
    