from flask_openapi3 import OpenAPI, Info, Tag
from flask import request, redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from Model import Produto, Session

from Schema import ProdutoBuscaPorIDSchema, ProdutoBuscaPorNomeSchema, ProdutoBuscaSchema, ProdutoDelSchema, ProdutoSchema, ProdutoViewSchema, apresenta_produto, apresenta_produtos, ListagemProdutosSchema
from Schema import ErrorSchema

from flask_cors import CORS

info = Info(title= "Tim Tim API", version="1.0.0")

app = OpenAPI(__name__, info=info)
CORS(app)


#Definindo as tags
home_tag = Tag(name="Documentação", description = "Descrição de documentação: Swagger")
produto_tag = Tag(name = "Produto", description = "Cadastro, visualização e remoção de produtos à base")

@app.get('/', tags = [home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação."""
    return redirect('/openapi')


@app.get('/produtos', tags=[produto_tag],
        responses={"200": ListagemProdutosSchema, "404": ErrorSchema})

def get_produtos():
    """Faz a busca por todos os produtos cadastrados
    Retorna uma apresentação da listagem de produtos."""

    session = Session()
    produtos = session.query(Produto).all()
    if not produtos:
        #se não há produtos cadastrados
        return {"produtos": []}, 200
    else:
        return apresenta_produtos(Produto), 200
    


@app.post('/produto', tags=[produto_tag],
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
        quantidade=form.quantidade,
        imagem=form.imagem
    )

    try:
        
        session = Session 
        session.add(produto)
        session.commit()
        return apresenta_produto(produto), 200
    
    except Exception as e:
    #caso erro fora do previsto
        return{"Não foi possível salvar novo item  :/"}, 400

    except IntegrityError as e:
    #duplicidade do nome é a provavel razão do IntegrityError
        return  {"Produto de mesmo nome e marca já salvo na base :( "}, 409

    

@app.get('/produtoId', tags=[produto_tag],
         responses={"200": ProdutoViewSchema, "404":ErrorSchema})

def get_produtoId(query: ProdutoBuscaPorIDSchema):
    """Faz uma busca por um produto a partir do id do produto
    Retorna uma apresentação dos produtos."""
    produto_id = query.id
    if not Produto:
        error_msg = "Produto não encontrado na base :( "
        return {"mesage": error_msg}, 404
    else:
        return apresenta_produto(Produto), 200
    

@app.delete('/delete/<int:id>', tags=[produto_tag],
            responses= {"200": ProdutoDelSchema, "404": ErrorSchema})
def del_produto(query: ProdutoBuscaPorIDSchema):
    """Deleta um produto a partir do Id informado
    Retorna uma mensagem de confirmação da remoção."""

    produto_id = unquote(unquote(query.nome))

    try:
        session = Session()
        count = session.query(Produto).filter(Produto.id == produto_id).delete()
        session.commit()
    
        if count:
            return {"mesage": "Produto removido", "id": produto_id},
        else:
        #se o produto não foi encontrado
            return {"Produto não encontrado na base :( "}, 404
    except Exception as e:
            return {"Erro": "Erro ao deletar o rpduto"}, 409
    

@app.get('/busca_produto', tags=[produto_tag],
         responses={"200": ListagemProdutosSchema, "404": ErrorSchema})
def busca_produto(query: ProdutoBuscaPorNomeSchema):
    """Faz a busca por produtos em que o termo passando  Produto a partir do nome do produto

    Retorna uma representação dos produtos.
    """
    termo = unquote(query.termo)
    session = Session()
    produtos = session.query(Produto).filter(Produto.nome.ilike(f"%{termo}%")).all()


    if not produtos:
        # se não há produtos cadastrados
        return {"produtos": []}, 200
    else:
        
        return apresenta_produtos(produtos), 200
      

if __name__=="__main__":
    app.run(debug=True)