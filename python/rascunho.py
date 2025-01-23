def split_teste(s):
    return s.upper().split(" ")


x = input("escreva um nome: ")
verificar = split_teste(x)
print(verificar[0])
