def len_lista (lista):
    if lista == []:
        return 0
    return 1 + len_lista(lista[1:])

if __name__ == '__main__':
    lista = [1,2,3,4,5,6,7,8,9]
    print(len_lista(lista))
