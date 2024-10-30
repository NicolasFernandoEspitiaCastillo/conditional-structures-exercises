#Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a mayor:

#Ingrese numero: 51
#Ingrese numero: 24
#24 51
#A continuación, escriba otro programa que haga lo mismo con tres números:

#Ingrese numero: 8
#Ingrese numero: 1
#Ingrese numero: 4
#1 4 8
#Finalmente, escriba un tercer programa que ordene cuatro números:

#Ingrese numero: 7
#Ingrese numero: 0
#Ingrese numero: 6
#Ingrese numero: 1
#0 1 6 7
#Recuerde que su programa debe entregar la solución correcta para cualquier combinación de números, no sólo para los ejemplos mostrados aquí.

#Hay más de una manera de resolver cada ejercicio.



# Programa para ordenar cuatro números

# Solicitar al usuario que ingrese cuatro números
numero1 = int(input("Ingrese numero: "))
numero2 = int(input("Ingrese numero: "))
numero3 = int(input("Ingrese numero: "))
numero4 = int(input("Ingrese numero: "))

# Ordenar y mostrar los números
numeros = [numero1, numero2, numero3, numero4]
numeros.sort()
print(*numeros)  # El asterisco (*) descompone la lista para imprimir los elementos
