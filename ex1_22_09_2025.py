class ErroImpar(Exception):
    pass
try:
    n = int(input("escreva um número inteiro: "))
    if n%2 != 0:
        raise ErroImpar
    else:
        print("o número",n,"é par")
except ErroImpar:
    print("ErroImpar:",n,"é um número ímpar")