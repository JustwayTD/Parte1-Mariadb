from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Date
import leFunciones


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

if __name__=="__main__":
   choo = menu()
    if choo == 1:
        palabra1 = input("Cual sera la palabra a agregar?\n")
        palabra2 = input("Y que significa eso?\n")
        agregar(palabra1,palabra2)
    elif choo == 2:
        palabra1 = input ("Cual palabra quieres editar?\n")
        palabra2 = input("Cual sera el nuevo significado?\n")
        editaMoh(palabra1,palabra2)
    elif choo == 3:
        palabra1 = input("Que palabra quieres eliminar?\n")
        eliminaMoh(palabra1)
    elif choo == 4:
        palabras = urbanDic()
        for palabras in palabras:
            print(palabras)
    elif choo == 5:
        palabra1 = input("De que palabra quieres el significado (case sensitive)")
        palabras = whatIsLove(palabra1)
        for palabras in palabras:
            print("Significa:", palabras)

