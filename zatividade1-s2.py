x = y = z = sx = sy = sz = sf = sm = f = m = s = n = sn = ss = gexs = gexn = geys = geyn = sexofs = sexofn = sexoms = sexomn = prss = prsn = prns = prnn = gezs = gezn =  0

while True:
    br = input('Brasil vai ganhar?(S/N): ').lower()
    ge = input('Geração(X/Y/Z): ').lower()
    if ge == 'x':
        x +=1
        if br == 's':
            sx +=1
    elif ge == 'y':
        y+=1
        if br == 's':
            sy +=1
    elif ge == 'z':
        z+=1
        if br == 's':
            sz +=1
    sexo = input('Sexo(F/M): ').lower()
    if sexo == 'f':
        f+=1
        if br == 's':
            sf +=1
    elif sexo == 'm':
        m+=1
        if br == 's':
            sm +=1
    pr = input('Pratica futebol?(S/N): ').lower()
    if pr == 's':
        s+=1
        if br == 's':
            ss +=1
    elif pr == 'n':
        n+=1
        if br == 's':
            sn +=1
    prox = input('Próxima pessoa?(S/N): ').lower()
    if prox != 's':
        break
if x != 0:
    gexs = (sx/x)*100
    gexn = 100 - gexs
if y != 0:
    geys = (sy/y)*100
    geyn = 100 - geys
if z != 0:
    gezs = (sz/z)*100
    gezn = 100 - gezs
if f != 0:
    sexofs = (sf/f)*100
    sexofn = 100 - sexofs
if m != 0:
    sexoms = (sm/m)*100
    sexomn = 100 - sexoms
if s != 0:
    prss = (ss/s)*100
    prsn = 100 - prss
if n != 0:
    prns = (sn/n)*100
    prnn = 100 - prns
print('Por geração:')
print(f'Geração X: {gexs:.0f}% Ganhar, {gexn:.0f}% Perder')
print(f'Geração Y: {geys:.0f}% Ganhar, {geyn:.0f}% Perder')
print(f'Geração Z: {gezs:.0f}% Ganhar, {gezn:.0f}% Perder')
print('Por sexo:')
print(f'Masculino: {sexoms:.0f}% Ganhar, {sexomn:.0f}% Perder')
print(f'Feminino: {sexofs:.0f}% Ganhar, {sexofn:.0f}% Perder')
print('Por prática de futebol:')
print(f'Sim: {prss:.0f}% Ganhar, {prsn:.0f}% Perder')
print(f'Não: {prns:.0f}% Ganhar, {prnn:.0f}% Perder')