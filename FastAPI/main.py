from fastapi import FastAPI

app = FastAPI()

vendas = {
    1:{"ITEM": "lata", "preco_unitario": 4, "quantidade": 5},
    2:{"ITEM": "garrafa 2l", "preco_unitario": 8, "quantidade": 12},
    3:{"ITEM": "lata mini", "preco_unitario": 10, "quantidade": 3},
    4:{"ITEM": "garrafa 750ml", "preco_unitario": 2, "quantidade": 6},
}

@app.get("/")
def home():
    return {"Vendas": len(vendas)}

@app.get("/vendas/{id_venda}")
def venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return{"ERRO": "Não existe esse valor no banco de dados."}