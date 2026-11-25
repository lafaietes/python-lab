"""
4. Escreva um programa em Python que peça ao utilizador um número inteiro n e
escreva no ecrã todas as potências de 2 com expoentes entre 0 e n, uma por linha.
"""

n = int(input("Indique um número inteiro: "))
i = 0

while i <= n:
    potencia = 2 ** i
    print(potencia)
    i += 1