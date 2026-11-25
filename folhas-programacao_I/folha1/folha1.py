# PROBLEMAS

""" 1. Escreva um programa em linguagem Python que leia dois números inteiros e
escreva no écran a sua soma, o seu produto, a subtração do primeiro pelo segundo,
a divisão do primeiro pelo segundo, o resto da divisão do primeiro pelo segundo, e
a potência do primeiro elevado ao segundo. """

"""
a = int(input("Insira um número: "))
b = int(input("Insira outro número "))

print(a, "+", b, "=", a+b)
print(a, "x", b, "=", a*b)
print(a, "-", b, "=", a-b)
print(a, "/", b, "=", a/b)
print(a, "%", b, "=", a%b)
print(str(a)+ "**"+ str(b), "=", a ** b)
"""


"""2. Escreva em linguagem Python um programa que leia dois números em vírgula
flutuante e imprima a sua soma, a sua diferença, o seu produto e o primeiro
elevado ao segundo."""

"""
c = float(input("Insira um número: "))
d = float(input("Insira outro número "))

print(c, "+", d, "=", c+d)
print(c, "-", d, "=", c-d)
print(c, "x", d, "=", c*d)
print(c, "**", d, "=", c**d)
"""


""" 3. Escreva em linguagem Python um programa que leia três números inteiros
correspondentes ao comprimento, largura e altura de um paralelepípedo e escreva
no écran o seu volume."""

"""
comprimento = int(input("Insira o comprimento do paralelepípedo: "))
largura = int(input("Insira a largura do paralelepípedo: "))
altura = int(input("Insira a altura do paralelepípedo: "))
print("O Volume do paralelepípedo é: ", comprimento * largura * altura)
"""



"""4. Escreva em linguagem Python um programa que leia três números inteiros e
escreva no écran a sua média. Altere o programa de forma ao valor ser o inteiro
que se obtém por truncar a parte decimal do resultado."""

"""
a = int(input("Insira um número: "))
b = int(input("Insira mais um número: "))
c = int(input("Insira mais um número: "))
media_inteira = (a + b + c) // 3
print(f"A média entre {a}, {b}, e {c} é {media_inteira}")
"""


"""5. Escreva em linguagem Python um programa que leia uma temperatura em graus
Fahrenheit e escreva a correspondente em graus Celsius.
A fórmula utilizada para a conversão de graus Fahrenheit em graus Celsius é:"""

"""
fahrenheit = float(input("Insira a temperatura em Fahrenheit: "))
celsius = (fahrenheit - 32) / 1.8
print(f"{fahrenheit}˚ Fahrenheit corresponde a {celsius:.1f}˚ Celsius.")
#print("{}˚ Fahrenheit corresponde a {:.1f}˚ Celsius.".format(fahrenheit, celsius))
"""



""" 6. Escreva em linguagem Python um programa que leia o ano de nascimento de
uma pessoa e escreva no écran a idade que terá no final do ano actual. Segue-se
um exemplo da interação com o computador.
Indique o ano de nascimento: 1972
No final de 2015 terá 42 ano(s)."""

"""
from datetime import datetime
ano_nascimento = int(input("Indique o ano de nascimento: "))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento
print(f"No final de {ano_atual} terá {idade} ano(s).")
"""


"""7. Escreva em linguagem Python um programa que determine o valor em cêntimos
de todas as moedas castanhas num mealheiro. Leia do teclado valores inteiros
representando o número de moedas de 5, 2, e 1 cêntimos."""

"""
moeda_1 = int(input("Insira a quantidade de moedas de 1 cêntimo: "))
moeda_2 = int(input("Insira a quantidade de moedas de 2 cêntimos: "))
moeda_5 = int(input("Insira a quantidade de moedas de 5 cêntimos: "))

total_centimos = moeda_1 + (moeda_2 * 2) + (moeda_5 * 5)
print(f"Tens no total {total_centimos} cêntimos no mealheiro.")
"""


"""8. Escreva em linguagem Python um programa que descreva um número inteiro
entre 0 e 999, em termos do número de centenas, número de dezenas e número
de unidades. Por exemplo, para 304 o resultado pretendido é “3 centenas 0
dezenas e 4 unidades”. """

"""
numero = int(input("Insira um número inteiro entre 0 e 999: "))
centena = numero // 100
resto = numero % 100
dezena = resto // 10
unidades = resto % 10
print(f"{centena} centenas, {dezena} dezenas e {unidades} unidades.")
"""


"""9. Escreva em linguagem Python um programa que leia um intervalo de tempo em
horas, minutos e segundos, e que depois imprima o número de segundos
equivalente. Por exemplo, 1 hora, 28 minutos e 42 segundos é equivalente a 5322
segundos. """

"""
horas = int(input("Indique as horas: "))
minutos = int(input("Indique os minutos: "))
segundos = int(input("Indique os segundos: "))
total_segundos = (horas * 3600) + (minutos * 60) + segundos
print(f"{horas} horas, {minutos} minutos e {segundos} segundos corresponde a {total_segundos} segundos.")
"""


""" 10. Desenvolva a versão inversa do problema anterior: lê um número
representando uma duração em segundos e imprime o seu equivalente em horas,
minutos e segundos. Por exemplo, 9999 segundos é equivalente a 2 horas, 46
minutos e 39 segundos"""

"""
numero = int(input("Insira o total de segundos: "))
horas = numero // 3600
resto = numero % 3600
minutos = resto // 60
segundos = resto % 60
print(f"{numero} segundos equivale a {horas} horas, {minutos} minutos e {segundos} segundos.")
"""
1,3,4,6,8