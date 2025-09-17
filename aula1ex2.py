i = int(input('idade: '))
if i > 70 or i >= 16 and i < 18:
    print("opcional")
elif i < 16:
    print("nao pode votar")
else:
    print("obrigado a votar")