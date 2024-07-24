from collections import deque


def pessoa_e_vendedora(nome):
    if nome == "peggy" or nome == "anuj":
        return True
    return False

def busca_vendedor_de_manga():
    fila_de_pesquisa = deque()
    grafo = dict()
    grafo["voce"] = ["alice", "bob", "claire"]
    grafo["bob"] = ["anuj", "peggy"]
    grafo["alice"] = ["peggy"]
    grafo["claire"] = ["jonny", "thom"]
    grafo["anuj"] = []
    grafo["peggy"] = []
    grafo["thom"] = []
    grafo["jonny"] = []

    fila_de_pesquisa += grafo["voce"]
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if pessoa_e_vendedora(pessoa):
            print(pessoa + ' é vendedora de manga!')
            return True
        else:
            fila_de_pesquisa += grafo[pessoa]

    return False
if __name__ == '__main__':
    busca_vendedor_de_manga()


