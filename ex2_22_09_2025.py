while True:
    try:
        n=int(input("escreva um número inteiro: "))
        r =10/n
        print("10/"+str(n)+" =",r)
        break
    except ValueError:
        print("Erro: não é um valor inteiro")
    except ZeroDivisionError:
        print("Erro: divisão por 0")

