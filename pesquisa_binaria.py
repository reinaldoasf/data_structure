def pesquisa_binaria(lista,item):
    baixo, alto = 0, len(lista) -1
    while baixo <= alto:
        meio = (alto+baixo)//2
        chute = lista[meio]
        if chute == item:
            return meio
        elif chute > item:
            alto = meio -1
        elif chute < item:
            baixo = meio+1
    return None
def pesquisa_binaria_recursiva(lista,item):
    def pesquisa_interna (baixo,alto):
        if baixo > alto:
            return None
        meio = (baixo+alto)//2
        chute = lista[meio]
        if chute == item:
            return meio
        elif chute > item:
            return pesquisa_interna(baixo,meio-1)
        elif chute < item:
            return pesquisa_interna(meio+1,alto)
    return pesquisa_interna(0,len(lista)-1)

if __name__ == "__main__":
    minha_lista = [1,2,3,4,5,6,77,312,317]
    print(pesquisa_binaria(minha_lista, 77))
    print(pesquisa_binaria_recursiva(minha_lista, 77))
