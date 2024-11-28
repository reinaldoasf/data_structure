def pesquisa_binaria(lista,item,baixo=0,alto=None):
    if alto == None:
        alto = len(lista)
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

def pesquisa_exponencial(lista,item):
    if lista[0] == item:
        return 0
    n = len(lista)
    idx = 1

    while idx < n and lista[idx] < item:
        idx*=2
    if lista[idx] == item:
        return idx
    return pesquisa_binaria(lista, item, idx//2, min(idx,n-1))

if __name__ == '__main__':
    lista_grande = list(range(1,9000))
    print(lista_grande[:101])
    target = 53

    indice = pesquisa_exponencial(lista_grande,target)
    print(f"O valor {target} está na posição {indice}")

        
    

