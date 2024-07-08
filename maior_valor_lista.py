def maior_valor(lista:list[int]) -> int:
    if len(lista) == 1:
        return lista[0]
    else:
        maior = maior_valor(lista[1:])
    if maior > lista[0]:
        return maior
    else:
        return lista[0]

if __name__ == '__main__':
    print(maior_valor([1,2,3,512,23,52,99]))
