from pydantic import BaseModel


class Pessoa(BaseModel):
    id: int
    nome: str
    idade: str
    email: str