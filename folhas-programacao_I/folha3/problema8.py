"""
8. Escreva um programa em Python que peça ao utilizador um número inteiro k e
escreva no ecrã o resultado do piatório das potências de 3 com expoente de 0 a k. 2
"""

k = int(input("Indique um número inteiro: "))
i = 0
produto = 1

while i <= k:
    produto *= 3 ** i
    i += 1

print(produto)