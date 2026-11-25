k = int(input("Indique um número inteiro: "))

i = 2
divisores = 0

while i < k:
    if k % i == 0:
        divisores += 1
    i += 1

if k > 1 and divisores == 0:
    print({k}, "é primo")
else:
    print(k, "não é primo")