from pydantic import BaseModel

# Classe  para API's
class Pessoa(BaseModel):
    id: int
    nome: str
    idade: str
    email: str