def notas(y,f):
    loop = True
    while loop:
        try:
            n = float(input(f"nota para o filme: {f} de {y}: "))
            if n < 0 or n > 10:
                raise Notainválida
            else:
                loop = False
                return n
        except Notainválida:
            print("NOTA INVÁLIDA")
        except ValueError:
            print("NOTA INVÁLIDA")
class Notainválida(Exception):
    pass
with open("filmes.txt", "r") as filmes:
    with open("filmes_avaliacao.txt", "w") as avaliacao:
        for linha in filmes:
            dados = linha.strip().split(",")
            nota = notas(dados[0],dados[1])
            avaliacao.write(f"{dados[0]},{dados[1]},{nota}\n")