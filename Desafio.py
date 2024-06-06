produtos = [
    {"nome": "Monitor","preco": 3.050},
    {"nome": "Fone de Ouvido", "preco": 8.00},
    {"nome": "Carregador", "preco": 15.00},
    {"nome": "Notebook", "preco": 3000.0},
    {"nome": "Placa Mãe", "preco": 85.00},
    {"nome": "Produto F" ,"preco": 130.00}
]

def Classificacao(preco):
    if preco < 50.00:
        return "Baixo"
    elif 50.00 <= preco <= 100.00:
        return "Médio"
    else:
        return "Alto"

def processamento(lista_produtos):
    for produto in lista_produtos:
        preco = produto["preco"]
        categoria = Classificacao(preco)
        produto["categoria"] = categoria

def MostrarProdutos(lista_produtos):
    for produto in lista_produtos:
        nome = produto["nome"]
        preco = produto["preco"]
        categoria = produto["categoria"]
        print(f"Nome do Produto {nome}, Preço Sugerido R${preco:.2f}, Categoria Atual {categoria}")

processamento(produtos)
MostrarProdutos(produtos)
