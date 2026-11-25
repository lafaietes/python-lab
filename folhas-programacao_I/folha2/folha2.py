# Folha 2
""" Escreva em linguagem Python um programa que leia um número e escreva no
ecrã se este é par ou ímpar. """
"""
numero = int(input("Insira um número: "))

if numero % 2 == 0:
    print("Par")
else:
        print("Ímpar")
        """

""" 2. Escreva em linguagem Python um programa que leia três números inteiros e
escreva no ecrã a soma dos que são pares e a soma dos que são ímpares """
"""
soma_pares = 0
soma_impares = 0

numero_1 = int(input("Insere um número: "))
numero_2 = int(input("Insere outro número: "))
numero_3 = int(input("Insere mais um número: "))

if numero_1 % 2 == 0:
    soma_pares += numero_1
else:
    soma_impares += numero_1

if numero_2 % 2 == 0:
    soma_pares += numero_2
else:
    soma_impares += numero_2

if numero_3 % 2 == 0:
    soma_pares += numero_3
else:
    soma_impares += numero_3

print(f"A soma dos números ímpares é {soma_impares} e dos pares é {soma_pares}.")
"""

""" 3. Escreva em linguagem Python um programa que leia dois números inteiros e
escreva no ecrã qual é o maior. Escreva uma variante do programa que indique,
adicionalmente, quando os número são iguais. Segue-se um exemplo da interacção
com o computador (variante).
Indique o primeiro número inteiro: 19
Indique o segundo número inteiro: 19
Os números são iguais. """
"""
numero1 = int(input("Indique o primeiro número inteiro: "))
numero2 = int(input("Indique o segundo número inteiro: "))

if numero1 > numero2:
    print(f"O maior número é {numero1}.")
elif numero1 == numero2:
    print("Os números são iguais.")
else:
     print(f"O maior número é o {numero2}.")
     """

"""4. Como alterava o programa anterior para determinar o maior número de três
números lidos. Faça duas versões do programa: uma que não lide com a igualdade
e outra que tenha em conta a igualdade entre os números. """
"""
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if numero1 == numero2 == numero3:
    print("Os três numeros são iguais.")
elif numero1 >= numero2 and numero1 >= numero3:
    print(f"O número {numero1} é o maior.")
elif numero2 >= numero1 >= numero3:
    print(f"O número {numero2} é o maior.")
else:
    print(f"O número {numero3} é o maior.")
"""

"""5. Escreva em linguagem Python um programa que leia um número inteiro positivo
(menor ou igual a 5) e escreva no ecrã a sua representação em numeração
romana. Segue-se um exemplo da interacção com o computador (em itálico os
dados introduzidos pelo utilizador).
Diga um número: 4
IV """
"""
numero = int(input("Indique um número de 1 a 5: "))

if numero == 1:
    print("I")
elif numero == 2:
    print("II")
elif numero == 3:
    print("III")
elif numero == 4:
    print("IV")
else numero == 5:
    print("V")
    """
"""
# Problema 6

dia_atual = 20
mes_atual = 10
ano_atual = 2026

dia_nascmento = int(input("Indique o seu dia de nascimento: "))
mes_nascimento = int(input("Indique o seu mês de nacimento: "))
ano_nascimento = int(input("Indique o seu ano de nascimento: "))

idade = ano_atual - ano_nascimento

if mes_atual < mes_nascimento:
    idade -= 1
elif mes_atual == mes_nascimento and dia_atual < dia_nascmento:
    idade -= 1

if idade == 1:
    print(f"Hoje tem {1} ano.")
else:
    print(f"Hoje tem {idade} anos.")
"""

"""
#Problema 7

num1 = int(input("Indique um número: "))
menor = num1
print(f"O menor número introduzido até agora é {menor}.")

num2 = int(input("Indique um número: "))
if num2 < num1:
    menor = num2
print(f"O menor número introduzido até agora é {menor}.")

num3 = int(input("Indique um número: "))
if num3 < menor:
    menor = num3
print(f"O menor número introduzido até agora é {menor}.")

num4 = int(input("Indique um número: "))
if num4 < menor:
    menor = num4
print(f"O menor número introduzido até agora é {menor}.")
"""
"""
# Problema 8
ano = int(input("Indique o ano: "))
if ano % 100 == 0:
    seculo = ano // 100
else:
    seculo = ano // 100 + 1

ano = int(input("Indique o ano: "))
seculo = ano - 1 // 100 + 1
print("Século:", seculo)

ano = int(input("Indique o ano: "))
seculo = ano // 100 + int(ano % 100 != 0)
print("Século:", seculo)
"""

# Problema 9
"""
ano = int(input("Indique o ano (>1900): "))
mes = int(input("Indique o mês (1-12): "))

bissexto = (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)

if mes == 2:
    if bissexto:
        print("O mês tem 29 dias.")
    else:
        print("O mês tem 28 dias.")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("O mês tem 30 dias.")
else:
    print("O mês tem 31 dias.")
"""
# Problema 10
"""10. Escreva um programa em Python que leia dois números inteiros e escreva no
écran o quadrado do maior a multiplicar pelo quadrado do primeiro. Se os números
forem iguais o programa deve escrever apenas “iguais”, e se forem ambos zero
deve escrever também “e ambos zero!"""
"""
numero_1 = int(input("Indique um número: "))
numero_2 = int(input("Indique outro número: "))

if numero_1 == numero_2:
    if numero_1 == 0:
        print("iguais e ambos zero.")
    else:
        print("iguais.")
else:
    if numero_1 > numero_2:
        maior = numero_1
    else:
        maior = numero_2

    resultado = (maior ** 2) * (numero_1 ** 2)
    print(resultado)
    """
"""
# Problema 11

# Problema 11 - Folha 2 (Sem usar break)

# 1. Leitura dos dados de entrada
ano = int(input("Indique o ano: "))
mes = int(input("Indique o mês (1-12): "))
dia = int(input("Indique o dia: "))
x = int(input("Indique o número de dias a avançar (x): "))

# 2. Somar os x dias ao dia inicial
dia = dia + x

# 3. Determinar os dias do mês inicial
bissexto = (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)

if mes == 2:
    dias_no_mes = 29 if bissexto else 28
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dias_no_mes = 30
else:
    dias_no_mes = 31

# 4. Ciclo controlado pela condição de ultrapassagem do mês
while dia > dias_no_mes:
    dia -= dias_no_mes
    mes += 1

    # Se passarmos de dezembro, avançamos para janeiro do ano seguinte
    if mes > 12:
        mes = 1
        ano += 1

    # Recalcular os dias do novo mês
    bissexto = (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)

    if mes == 2:
        dias_no_mes = 29 if bissexto else 28
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dias_no_mes = 30
    else:
        dias_no_mes = 31

# 5. Apresentação da nova data
print(f"Nova data ({x} dias depois): {dia}/{mes}/{ano}")
"""
1,10,7,2