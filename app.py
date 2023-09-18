from flask_openapi3 import OpenAPI, Info, Tag
from flask import request, redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from Model import Produto, Session
from logger import logger
from Schema import *
from Schema import ErrorSchema

from flask_cors import CORS

info = Info(title="Tim Tim API", version="1.0.0")

app = OpenAPI(__name__, info=info)
CORS(app)


# Definindo as tags
home_tag = Tag(name="Documentação",
               description="Descrição de documentação: Swagger")

produto_tag = Tag(
    name="Produto", description="Cadastro, visualização e remoção de produtos à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação."""
    return redirect('/openapi')

#funcionando
@app.get('/produtos', tags=[produto_tag],
         responses={"200": ListagemProdutosSchema, "404": ErrorSchema})
def get_produtos():
    """Faz a busca por todos os produtos cadastrados
    Retorna uma apresentação da listagem de produtos."""

    logger.info(f"Coletando produtos ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    produtos = session.query(Produto).all()

    if not Produto:
        # se não há produtos cadastrados
        return {"produtos": []}, 200
    else:
        logger.info(f"%d produtos encontrados" % len(produtos))
        # retorna a representação de produto
        return apresenta_produtos(produtos), 200


# funcionando
@app.post('/post_produto', tags=[produto_tag],
          responses={"200": ProdutoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_produto(form: ProdutoSchema):
    """Cadastra um novo Produto à base de dados"""
    """Retorna uma apresentação dos produtos"""

    print(form)
    produto = Produto(
        nome=form.nome,
        descricao=form.descricao,
        preco=form.preco,
        avaliacao=form.avaliacao,
        categoria=form.categoria,
        quantidade=form.quantidade
    )
    logger.info(f"Adicionando produto de nome: '{produto.nome}'")

    try:
        # criando conexão com a base
        session = Session()
        # adicionando produto
        session.add(produto)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.info("Adicionado produto: %s" % produto)
        return apresenta_produto(produto), 200

    except Exception as e:
        # caso erro fora do previsto
        error_msg = "Não foi possível cadastrar novo item  :("
        logger.warning(
            f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"mesage": error_msg}, 400

    except IntegrityError as e:
        # duplicidade do nome é a provavel razão do IntegrityError
        error_msg = "Produto de mesmo nome e categoria já salvo na base  :/ "
        logger.warning(
            f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"mesage": error_msg}, 409


@app.get('/produto_id', tags=[produto_tag],
         responses={"200": ProdutoViewSchema, "404": ErrorSchema})
def get_produtoId(query: ProdutoBuscaPorIDSchema):
    """Faz uma busca por um produto a partir do id do produto
    Retorna uma apresentação dos produtos."""
    produto_id = query.id
    logger.info(f"Coletando dados sobre produto #{produto_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    produto = session.query(Produto).filter(Produto.id == produto_id).first()

    if not Produto:
        # se o produto não foi encontrado
        error_msg = "Produto não encontrado na base :( "
        logger.warning(f"Erro ao buscar produto '{produto_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.info("Produto econtrado: %s" % produto)
        # retorna a representação de produto
        return apresenta_produto(Produto), 200

# funcionando
@app.delete('/delete_produto', tags=[produto_tag],
            responses={"200": ProdutoDelSchema, "404": ErrorSchema})
def del_produto(query: ProdutoBuscaPorIDSchema):
    """Deleta um produto a partir do id informado
    Retorna uma mensagem de confirmação da remoção."""

    produto_id = query.id
    logger.info(f"Deletando dados sobre produto #{produto_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Produto).filter(Produto.id == produto_id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.info(f"Deletado produto #{produto_id}")
        return {"mesage": "Produto removido", "id": produto_id}, 200
    else:
        # se o produto não foi encontrado
        error_msg = "Produto não encontrado na base :( "
        logger.warning(f"Erro ao deletar produto #'{produto_id}', {error_msg}")
        return {"mesage": error_msg}, 404

# Funcionando
@app.get('/busca_produto', tags=[produto_tag],
         responses={"200": ListagemProdutosSchema, "404": ErrorSchema})
def busca_produto(query: ProdutoBuscaPorNomeSchema):
    """Faz a busca por produtos em que o termo passando  Produto a partir do nome do produto

    Retorna uma representação dos produtos.
    """
    termo = unquote(query.termo)
    logger.info(f"Fazendo a busca por nome com o termo: {termo}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    produtos = session.query(Produto).filter(
        Produto.nome.ilike(f"%{termo}%")).all()

    if not produtos:
        # se não há produtos cadastrados
        return {"produtos": []}, 200
    else:
        logger.info(f"%d rodutos econtrados" % len(produtos))
        # retorna a representação de produto
        return apresenta_produtos(produtos), 200
    

@app.put('/put_produto', tags=[produto_tag],
          responses={"200": ProdutoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def update_produto(query: ProdutoDelSchema,form: ProdutoUpdateSchema):
    """Alterar Produto à base de dados"""
    """Retorna uma apresentação dos produtos"""

    print(form)
    produto = Produto(
        nome=form.nome,
        descricao=form.descricao,
        preco=form.preco,
        avaliacao=form.avaliacao,
        categoria=form.categoria,
        quantidade=form.quantidade
    )
    logger.info(f"Adicionando produto de nome: '{produto.nome}'")

    try:
        # criando conexão com a base
        session = Session()
        # adicionando produto
        session.add(produto)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.info("Adicionado produto: %s" % produto)
        return apresenta_produto(produto), 200

    except Exception as e:
        # caso erro fora do previsto
        error_msg = "Não foi possível cadastrar novo item  :("
        logger.warning(
            f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"mesage": error_msg}, 400

    except IntegrityError as e:
        # duplicidade do nome é a provavel razão do IntegrityError
        error_msg = "Produto de mesmo nome e categoria já salvo na base  :/ "
        logger.warning(
            f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"mesage": error_msg}, 409




if __name__ == "__main__":
    app.run(debug=True)
