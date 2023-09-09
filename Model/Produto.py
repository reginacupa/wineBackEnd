from sqlalchemy import Column, String, Integer, Float, UniqueConstraint
from sqlalchemy.orm import relationship
from typing import Union


from Model import Base

class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(30), default='Vinho')
    descricao = Column(String(300), nullable=True)
    preco = Column(Float)
    avaliacao = Column(Float)
    categoria = Column(String(80))
    quantidade = Column(Integer)
    imagem = Column(String)

    def __init__(self, nome: str, descricao: str, preco: float, avaliacao: float, categoria: str, quantidade: int,   imagem: str):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.avaliacao = avaliacao
        self.categoria = categoria
        self.quantidade = quantidade
        self.imagem = imagem

def to_dict(self):
        """
        Retorna a representação em dicionário do Objeto Produto.
        """
        return{
            "id": self.id,
            "nome": self.nome,
            "marca": self.marca,
            "categoria": self.categoria,
            "descricao": self.descricao,
            "preco": self.preco,
        }

def to_dict(self):
        """
        Retorna a representação em dicionário do Objeto Produto.
        """
        return{
            "id": self.id,
            "nome": self.nome,
            "marca": self.marca,
            "categoria": self.categoria,
            "descricao": self.descricao,
            "preco": self.preco,
        
        
        }

def __repr__(self):
    """
    Retorna uma representação do Produto em forma de texto.
    """
    return f"Product(id={self.id}, nome='{self.nome}', preco={self.preco}, marca='{self.marca}', categoria='{self.categoria}')"



