from pydantic import BaseModel

class ErrorSchema (BaseModel):
    mesage: str = 'Erro! Tente Novamente'

    