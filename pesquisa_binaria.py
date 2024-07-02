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

if __name__ == "__main__":
    minha_lista = [1,2,3,4,5,6,77,312,317]
    print(pesquisa_binaria(minha_lista, 77))
    print(pesquisa_binaria(minha_lista,9))
