def media(n1,n2,n3):
    m = (n1 +n2 +n3)/3
    return m
aprovados = open("aprovados.txt", "w")
reprovados = open("reprovados.txt", "w")
exame = open("exame.txt", "w")
with open("notas.txt", "r") as notas:
    for linha in notas:
        dados = linha.strip().split(",")
        nome = dados[0]
        med = media(float(dados[1]),float(dados[2]),float(dados[3]))
        if med >= 7:
            aprovados.write(f"{nome}, Media: {med:.2f}\n")
        elif med < 5:
            reprovados.write(f"{nome}, Media: {med:.2f}\n")
        else:
            exame.write(f"{nome}, Media: {med:.2f}\n")
