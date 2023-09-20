from pydantic import BaseModel
from typing import Optional, List
from Model.Produto import Produto


class ProdutoSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    nome: str = "Montes Alpha - Cabernet Sauavignon"
    descricao:  str = "Verdadeiro clássico da América do Sul, o Montes Alpha foi o primeiro grande tinto chileno, inspirado nos melhores vinhos de Bordeaux.  Um vinho excelente, de imbatível relação qualidade/preço"
    preco: float = "259.23"
    avaliacao: float = 8.8
    categoria: str = "Cabernet Sauavignon"
    quantidade:  int = 25
    imagem: str = ("https://cdn.mistral.com.br/products/35015/img_m_35015.png")


class ProdutoViewSchema(BaseModel):
    """ Define como um produto será retornado: produto.
    """
    id: int = 1
    nome: str = "Montes Alpha"
    descricao: str = "Verdadeiro clássico da América do Sul, o Montes Alpha foi o primeiro grande tinto chileno, inspirado nos melhores vinhos de Bordeaux.  Um vinho excelente, de imbatível relação qualidade/preço"
    preco: float = 259.23
    avaliacao: float = 8.8
    categoria: str = "Cabernet Sauavignon"
    quantidade: Optional[int] = 25
    imagem: str = ("https://cdn.mistral.com.br/products/35015/img_m_35015.png")



class ProdutoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    nome: str = "Montes Alpha"


class ListagemProdutosSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    produtos: List[ProdutoViewSchema]


class ProdutoUpdateSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    nome: str = "Montes Alpha - Cabernet Sauavignon"
    descricao:  str = "Verdadeiro clássico da América do Sul, o Montes Alpha foi o primeiro grande tinto chileno, inspirado nos melhores vinhos de Bordeaux.  Um vinho excelente, de imbatível relação qualidade/preço"
    preco: float = "259.23"
    avaliacao: float = 8.8
    categoria: str = "Cabernet Sauavignon"
    quantidade:  int = 25
    imagem: str = ("https://cdn.mistral.com.br/products/35015/img_m_35015.png")


def apresenta_produtos(produtos: List[Produto]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for produto in produtos:
        result.append({
            "id": produto.id,
            "nome": produto.nome,
            "descricao": produto.descricao,
            "preco": produto.preco,
            "avaliacao": produto.avaliacao,
            "categoria": produto.categoria,
            "quantidade": produto.quantidade,
            "imagem": produto.imagem        

        })

    return {"produtos": result}


class ProdutoBuscaPorIDSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no ID do produto.
    """
    id: int = "1"


class ProdutoBuscaPorNomeSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    termo: str = "Malbec"


class ProdutoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str = "Produto removido com sucesso"
    id: int = "1"


def apresenta_produto(produto: Produto):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {

        "id": produto.id,
        "nome": produto.nome,
        "descricao": produto.descricao,
        "preco": produto.preco,
        "avaliacao": produto.avaliacao,
        "categoria": produto.categoria,
        "quantidade": produto.quantidade,
        "imagem": produto.imagem

    }
