
k = int(input("Indique um número inteiro: "))
contador = 0

for i in range(k + 1):
    if i % 3 == 0 and i % 2 != 0:
        contador += 1

print(contador)
