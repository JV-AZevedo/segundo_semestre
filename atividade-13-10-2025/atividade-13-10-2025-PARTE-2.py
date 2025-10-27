e = []
with open("filmes_indicacao.txt", "w") as indicacao:
    for i in range(5):
        m = -1
        with open("filmes_avaliacao.txt", "r") as filmesav:
            for linhas in filmesav:
                notas = linhas.strip().split(",")
                if notas[0] in e:
                        continue
                elif float(notas[2]) > m:    
                        m = float(notas[2])
                        l = []
                        l.append(notas[0])
                        l.append(notas[1])
                        l.append(notas[2])
            e.append(l[0])
            indicacao.write(f"{l[0]},{l[1]},{l[2]}\n")