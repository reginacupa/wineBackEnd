from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
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
home_tag = Tag(name="Documentação", description = "Seleção de documentação: Swagger")
produto_tag = Tag(name = "Produto", description = "Adição, visualização e remoção de produtos à base")

@app.get('/', tags = [home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação."""
    return redirect('/openapi')



@app.post('/produto', tags=[produto_tag],
    responses={"200": ProdutoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_produto(form: ProdutoSchema):
    """Adiciona um novo Produto à base de dados"""
    """Retorna uma apresentação dos produtos"""

    print(form)
    produto = Produto(
        nome=form.nome,
        descricacao=form.descricacao,
        preco=form.preco,
        avaliacao=form.avaliacao,
        categoria=form.categoria,
        quantidade=form.quantidade
 )  
    
@app.get('/produtos', tags=[produto_tag],
         responses={"200": ListagemProdutosSchema, "404": ErrorSchema})
def get_produtos():
    """Faz a busca por todos os produtos cadastrados
    Retorna uma apresentação da listagem de produtos."""
    if not Produto:
        #se não há produtos cadastrados
        return {"produtos": []}, 200
    else:
        return apresenta_produto(Produto), 200
    

@app.get('/produto', tags=[produto_tag],
         responses={"200": ProdutoViewSchema, "404":ErrorSchema})

def get_produto(query: ProdutoBuscaPorIDSchema):
    """Faz uma busca por um produto a partir do id do produto
    Retorna uma apresentação dos produtos."""
    produto_id = query.id
    if not Produto:
        error_msg = "Produto não encontrado na base :( "
        return {"mesage": error_msg}, 404
    else:
        return apresenta_produto(Produto), 200
    
@app.delete('/produto', tags=[produto_tag],
            responses= {"200": ProdutoDelSchema, "404": ErrorSchema})
def del_produto(query: ProdutoBuscaPorIDSchema):
    """Deleta um produto a partir do Id informado
    Retorna uma mensagem de confirmação da remoção."""
    produto_nome = unquote(unquote(query.nome))
    
    if produto_nome:
        return {"mesage": "Produto removido", "id": produto_nome},
    else:
        #se o produto não foi encontrado
        error_msg = "Produto não encontrado na base :( "
        return {"mesage": error_msg}, 404
    
@app.get('/busca_produto', tags=[produto_tag],
         responses={"200": ListagemProdutosSchema, "404": ErrorSchema})
def busca_produto(query: ProdutoBuscaPorNomeSchema):
    """Faz a busca por produtos em que o termo passando  Produto a partir do id do produto

    Retorna uma representação dos produtos e comentários associados.
    """
    termo = unquote(query.termo)
    if not Produto:
        # se não há produtos cadastrados
        return {"produto": []}, 200
    else:
        
        return apresenta_produtos(Produto), 200
      

if __name__=="__main__":
    app.run(debug=True)