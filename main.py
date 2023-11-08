import uvicorn
from fastapi import FastAPI,Response
from classmodels import Pessoa

app = FastAPI()


@app.get("/get")
def get_pessoa():
    return "Olá mundo !"

@app.post("/post")
def post_pessoa(pessoa: Pessoa) -> str:
    return f"Dados:  Nome: {pessoa.nome}  Idade: {pessoa.idade}  E-mail: {pessoa.email}"


@app.delete("/delete")
def delete_pessoa() -> str:
    return "Olá mundo !"

@app.put("/put")
def put_pessoa() -> str:
    return "Olá mundo !"


if __name__ == "__main__":
    uvicorn.run(app,port=8000)