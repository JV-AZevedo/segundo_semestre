n = 1
with open("filmes_indicacao.txt", "r") as top:
    for linhas in top:
        s = linhas.strip()
        print(str(n)+ "º",s)
        n += 1