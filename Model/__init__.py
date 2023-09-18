from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
import os

from Model.Base import Base
from Model.Produto import Produto

db_path = 'database/'

if not os.path.exists(db_path):
    os.makedirs(db_path)

db_url = 'sqlite:///%s/db.sqlite3' % db_path

engine = create_engine(db_url, echo=False)

Session = sessionmaker(bind=engine)

if not database_exists(db_url):
    create_database(db_url)

Base.metadata.create_all(engine)
session=Session()
itens=[   
    {   "nome": "Montes Alpha",
        "descricao": "Verdadeiro clássico da América do Sul, o Montes Alpha foi o primeiro grande tinto chileno, inspirado nos melhores vinhos de Bordeaux.  Um vinho excelente, de imbatível relação qualidade/preço",
        "preco": "259.23",
        "avaliacao": 8.8,
        "categoria": "Cabernet Sauavignon",
        "quantidade": 25},

    
    {
        "nome": "Alamos",
        "descricao": "O consagrado Alamos Malbec é um dos mais emblematicos vinhos da Argentina. Sem duvuda um dos eternos achados do Novo Mundo e um dos mais clássicos Malbecs da Argentina. Muito recomendado!",
        "preco": "113.32",
        "avaliacao": 7.8,
        "categoria": "Malbec",
        "quantidade": 40},

    {
        "nome": "Angélica Zapata",
        "descricao": "Complexo e sofisticado, o cativante Angelica Zapata Merlot é um pouco mais macio e sedoso que cultuado Angelica Malbec, sendo uma companhia perfeita para massas, pizzas e até hambúrgueres. Um vinho de pequena produção, antes vendido somente na Argentina, é uma verdadeira revelação para quem ainda não provou um grande Merlot deste país.",
        "preco": "268.08",
        "avaliacao": 8.4,
        "categoria": "Merlot",
        "quantidade": 15},

    {
        "nome": "Catena",
        "descricao": "Este é o tinto que mostrou ao mundo o potencial da casta Malbec para originar vinhos de classe mundial.  Eleito mais de uma vez um dos “100 Melhores Vinhos do Mundo” pela Wine Spectator, é uma referência absoluta.",
        "preco": "187.38",
        "avaliacao": 8.3,
        "categoria": "Malbec",
        "quantidade": 28},

    {
        "nome": "Caymus",
        "descricao": "Um dos ícones do vinho californiano, o excelente Caymus Cabernet Sauvignon goza de imenso prestígio e sempre merece ótimas notas da imprensa especializada. Além da grande estrutura, potência e concentração dos melhores Cabernets americano, ele também é muito elegante e refinado, com grande classe e complexidade. É um vinho que pode envelhecer muitos anos.",
        "preco": "1326.01",
        "avaliacao": 9.2,
        "categoria": "Cabernet Sauavignon",
        "quantidade": 17},

    {
        "nome": "Vaze Feliz Shiraz",
        "descricao": "Segundo James Halliday, Cabernet Sauvignon pode ser a queridinha de Margaret River, mas alguns Shiraz como este deixam a região orgulhosa. Este belíssimo tinto tem um estilo mais elegante que os Shiraz de Barossa Valley, combinando taninos abundantes, suculentas notas de fruta e ótima acidez. Segundo a celebrada enóloga Virginia Willcock, as uvas são colhidas -al dente- e as barricas onde o vinho matura são neutras, para garantir o frescor e a pureza da fruta.",
        "preco": "364.25",
        "avaliacao": 8.5,
        "categoria": "Cabernet Sauavignon",
        "quantidade": 29}
    ]

for item in itens:
    novo_item = Produto (
        nome=item['nome'],
        descricao=item['descricao'],
        preco=item['preco'],
        avaliacao=item['avaliacao'],
        categoria=item['categoria'],
        quantidade=item['quantidade']
    )
    session.add(novo_item)
session.commit()









