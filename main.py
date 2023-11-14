import uvicorn
from fastapi import FastAPI,Response
from classmodels import Pessoa

# Array Teste, para testes de POST.
pessoas = []

#Função para mostrar todos os dados do Array Acima.
def mostrarDados():
    for pessoa in pessoas:
        print(f"ID: {pessoa['id']} NOME: {pessoa['nome']} IDADE: {pessoa['idade']} EMAIL: {pessoa['email']}")

# Criando APP instanciando.
app = FastAPI()


# API METODO GET
@app.get("/get")
def get_pessoa():
    return " Get Ok "

#API METODO POST
@app.post("/post")
def post_pessoa(pessoa: Pessoa) -> str:

    pessoas.append({
        "id":pessoa.id,
        "nome":pessoa.nome,
        "idade":pessoa.idade,
        "email":pessoa.email
    })

    mostrarDados()

    return f"Dados:  Nome: {pessoa.nome}  Idade: {pessoa.idade}  E-mail: {pessoa.email}"

# API METODO DELETE
@app.delete("/delete")
def delete_pessoa() -> str:
    return " Delete Ok "

# API METODO PUT
@app.put("/put")
def put_pessoa() -> str:
    return " Put Ok"

# START API's
if __name__ == "__main__":
    uvicorn.run(app,port=8000)