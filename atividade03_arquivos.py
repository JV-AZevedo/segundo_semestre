def media(m,nome):
    loop = True
    while loop:
        try:
            n = float(input(f"{nome}. Sua nota do exame: "))
            if n > 10 or n < 0:
                raise NotaInvalida
            else:
                loop = False
                r = (m+n)/2
                return r
        except ValueError:
            print("NOTA INVÁLIDA")
        except NotaInvalida:
            print("NOTA INVÁLIDA")
class NotaInvalida(Exception):
    pass
aprovados = open("aprovados.txt", "a")
reprovados = open("reprovados.txt", "a")
with open("exame.txt", "r") as exame:
    for linha in exame:
        dados = linha.strip().split(",")
        nome = dados[0]
        mediaf = media(float(dados[1].replace("Media:","")),nome)
        if mediaf >= 5:
            aprovados.write(f"{nome}, Media: {mediaf:.2f}, Aprovado apos exame\n")
        else:
            reprovados.write(f"{nome}, Media: {mediaf:.2f}, Reprovado apos exame\n")