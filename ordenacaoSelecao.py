def buscaMenor(arr):
    menor = arr[0]
    menorIndice = 0

    for i in range (1,len(arr)):
        if arr[i]<menor:
            menorIndice = i
    return menorIndice

def ordenacaoPorSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

if __name__ == '__main__':
    disorderedList = [1,4,6,2,9,12,42,18]
    print(disorderedList)
    orderedList = ordenacaoPorSelecao(disorderedList)
    print(orderedList)
