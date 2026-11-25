#Problema 5

"""
Escreva uma função ler_inteiro que lê, garantidamente, um inteiro do utilizador.
A função deve pedir a informação ao utilizador até que seja fornecido um número
inteiro. Faça um programa que teste convenientemente a função desenvolvida.
"""


def ler_inteiro():
    while True:
        try:
            numero = int(input("Introduza um número inteiro: "))
            return numero
        except ValueError:
            print("Valor inválido! Try another vez.")
