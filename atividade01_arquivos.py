def valido(n, x):
    loop = True
    while loop:
        try:
            n = float(input("nota "+str(x)+": "))
            if n > 10 or n < 0:
                raise NotaInvalida
            else:
                loop = False
                return n
        except ValueError:
            print("NOTA INVÁLIDA")
        except NotaInvalida:
            print("NOTA INVÁLIDA")
class NotaInvalida(Exception):
    pass
n1 = n2 = n3 = None
with open("notas.txt", "w") as notas:
    while True:
        nome = input("nome: ").capitalize()
        n1 = valido(n1, 1)
        n2 = valido(n2, 2)
        n3 = valido(n3, 3)
        notas.write(f"{nome},{n1},{n2},{n3}\n")
        cont = input("deseja continuar?(S/N): ").upper()
        if cont == "N":
            break