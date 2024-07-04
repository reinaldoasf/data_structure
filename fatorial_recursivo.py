def fatorial(number):
    if number == 1:
        return 1
    else:
        return number*fatorial(number-1)

if __name__ == '__main__':
    num = int(input("Digite o numero inteiro positivo para saber o fatorial\n"))
    while num <1:
        num = input("Digite o numero inteiro positivo para saber o fatorial\n")
    print(f"O fatorial de {num} é: \n{fatorial(num)}")