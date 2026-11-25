terminar = "n"

while terminar != "s":

    numero = float(input("Indique um número decimal: "))

    print("Parte inteira:", int(numero))
    
    terminar = input("Deseja terminar? (s/n): ")