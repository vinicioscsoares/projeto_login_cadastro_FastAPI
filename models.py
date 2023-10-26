from sqlalchemy import create_engine, Column, Integer, Boolean, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymysql import *
import datetime

USUARIO = 'root'
SENHA =''
HOST = 'localhost'
BANCO = 'aula_fastapi'
PORT = '3306'

CONN = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}'


engine = create_engine(CONN, echo=True)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Pessoa(Base):
  __tablename__= 'Pessoa'
  id = Column(Integer,primary_key=True)
  nome = Column(Integer,primary_key=True)
  usuario = Column(String(50))
  senha = Column(String(100))

  
class Tokens(Base):
  __tablename__ = 'Tokens'
  id = Column(Integer,primary_key=True)
  id_pessoa = Column(Integer, ForeignKey('Pessoa.id'))
  token = Column(String(100))
  data = Column(DateTime, default=datetime.datetime.utcnow())
  
Base.metadata.create_all(engine)