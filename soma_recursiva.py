def soma_recursiva(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + soma_recursiva(lista[1:])

if __name__ == "__main__":
    lista = [1,2,3,4,5,6,7,8,9]
    print(soma_recursiva(lista))
