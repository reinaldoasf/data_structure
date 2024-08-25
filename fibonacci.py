def fib(n:int)->int:
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

if __name__ == "__main__":
    x = input("Digite o numero de termos de fibonacci")
    print(fib(int(x)))
