from random import randint
def quicksort(lista:list) -> list:
    if len(lista)<2:
        return lista
    elif len(lista) == 2:
        if lista[1]<lista[0]:
            lista[0], lista[1] = lista[1], lista[0]
        return lista

    indice_pivo = randint(0,len(lista)-1)
    pivo = lista[indice_pivo]
    menor = [x for idx,x in enumerate(lista) if x<=pivo and indice_pivo!=idx]
    maior = [x for idx,x in enumerate(lista) if x>pivo and indice_pivo!=idx]

    return quicksort(menor)+[pivo]+quicksort(maior)

if __name__ == "__main__":
    minha_lista = [1,52,63234,-1235,753,123,8844,123,123123,7456]

    print(minha_lista)
    print(quicksort(minha_lista))
