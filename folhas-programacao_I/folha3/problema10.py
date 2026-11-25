
k = int(input("Indique um número inteiro: "))
i = 0
contador = 0

while i<=k:
    if i % 2 != 0:
        contador += 1
    i += 1

print(contador)
