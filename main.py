#Escriba un programa que determine si el número entero ingresado por el usuario es par o no.

#ngrese un número: 4
#Su número es par
#Ingrese un número: 3
#Su número es impar



# Programa para determinar si un número es par o impar

# Solicitar al usuario que ingrese un número entero
numero = int(input("Ingrese un número: "))

# Verificar si el número es par o impar
if numero % 2 == 0:
    print("Su número es par")
else:
    print("Su número es impar")
