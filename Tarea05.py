def menu():
    print("Bienvenido")
    print("Digite la opcion que desea realizar")
    print("1. Calcular el area de un circulo")
    print("2. Salir")
    op = input ("Escriba la opcion:")
    op = int(op)
    if op==1: Area_de_circulo()
    else: exit()

def Area_de_circulo():
    import math
    print("")
    print("Para calcular el area de un circulo, necesitamos conocer su radio.")
    print("Por favor, Ingrese el valor del radio del circulo:")
    r = float (input())
    a= math.pi * (r*r)
    print("El area del circulo de ",r," es: ",a)
    print("")
    menu()
menu()