# Classificação de Produtos

Este script classifica uma lista de produtos com base em seus preços e exibe os produtos junto com suas classificações.

## Descrição

O script contém uma lista de dicionários, onde cada dicionário representa um produto com seu nome e preço. Ele classifica cada produto em uma das três categorias: "Baixo", "Médio" ou "Alto", de acordo com o preço. A classificação é feita da seguinte maneira:

- **Baixo**: Preços menores que R$ 50,00
- **Médio**: Preços entre R$ 50,00 e R$ 100,00 (inclusive)
- **Alto**: Preços acima de R$ 100,00

## Funções

### Classificacao(preco)

Esta função recebe um preço e retorna a categoria correspondente:

- **Parâmetro**: `preco` (float) - O preço do produto.
- **Retorno**: `str` - A categoria do produto ("Baixo", "Médio" ou "Alto").

### processamento(lista_produtos)

Esta função recebe uma lista de produtos, processa cada produto para determinar sua categoria e adiciona essa informação ao dicionário do produto.

- **Parâmetro**: `lista_produtos` (list) - A lista de produtos a ser processada.

### MostrarProdutos(lista_produtos)

Esta função exibe todos os produtos da lista com seus nomes, preços formatados e categorias.

- **Parâmetro**: `lista_produtos` (list) - A lista de produtos a ser exibida.

## Uso

Para usar este script, basta chamar a função `processamento` passando a lista de produtos e, em seguida, chamar a função `MostrarProdutos` para exibir os produtos classificados. Aqui está um exemplo de como o script funciona:

```python
produtos = [
    {"nome": "Monitor","preco": 3050.00},
    {"nome": "Fone de Ouvido", "preco": 8.00},
    {"nome": "Carregador", "preco": 15.00},
    {"nome": "Notebook", "preco": 3000.00},
    {"nome": "Placa Mãe", "preco": 85.00},
    {"nome": "Produto F" ,"preco": 130.00}
]

processamento(produtos)
MostrarProdutos(produtos)

Exemplo de Saída

Nome: Monitor, Preço: R$3050.00, Categoria: Alto
Nome: Fone de Ouvido, Preço: R$8.00, Categoria: Baixo
Nome: Carregador, Preço: R$15.00, Categoria: Baixo
Nome: Notebook, Preço: R$3000.00, Categoria: Alto
Nome: Placa Mãe, Preço: R$85.00, Categoria: Médio
Nome: Produto F, Preço: R$130.00, Categoria: Alto

