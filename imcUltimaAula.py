l = []
while True:
    nome = input("Nome: ")
    l.append(nome)
    idade = input("Idade: ")
    l.append(idade)
    erro = True
    while erro == True:
        try:
            peso = float(input("Peso: "))
            altura = float(input("Altura(m): "))
        except ValueError:
            print("valor inválido")
        else:
            erro = False
    imc = peso/(altura**2)
    if imc < 16:
        l.append("Baixo peso Grau I")
    elif imc < 16.99: 
        l.append("Baixo peso Grau II")
    elif imc < 18.49:
        l.append("Baixo peso Grau III")
    elif imc < 24.99:
        l.append("Peso adequado")
    elif imc < 29.99:
        l.append("Sobrepeso")
    elif imc < 34.99:
        l.append("Obesidade grau I")
    elif imc < 39.99:
        l.append("Obesidade grau II")
    else:
        l.append("Obesidade grau III")
    loop = input("Próxima pessoa(S/N)?: ").upper()
    if loop == "N":
        for i in range(0,len(l),3):
            print("Cliente:",l[i],"-",l[i+1],"anos -",l[i+2])
        break 