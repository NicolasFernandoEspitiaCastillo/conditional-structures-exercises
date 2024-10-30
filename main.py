#Escriba un programa que pida dos números enteros y que calcule la división, indicando si la división es exacta o no.

#Dividendo: 14
#Divisor: 5

#La división no es exacta.
#Cociente: 2
#Resto: 4
#Dividendo: 100
#Divisor: 10

#La división es exacta.
#Cociente: 10
#Resto: 0




# Programa para calcular la división y determinar si es exacta

# Solicitar al usuario el dividendo y el divisor
dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))

# Realizar la división
cociente = dividendo // divisor
resto = dividendo % divisor

# Mostrar si la división es exacta o no
if resto == 0:
    print("La división es exacta.")
else:
    print("La división no es exacta.")

# Mostrar el cociente y el resto
print(f"Cociente: {cociente}")
print(f"Resto: {resto}")



