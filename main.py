#Los tres lados a, b y c de un triángulo deben satisfacer la desigualdad triangular: cada uno de los lados no puede ser más largo que la suma de los otros dos.

#Escriba un programa que reciba como entrada los tres lados de un triángulo, e indique:

#si acaso el triángulo es inválido; y
#si no lo es, qué tipo de triángulo es.
#Ingrese a: 3.9
#Ingrese b: 6.0
#Ingrese c: 1.2
#No es un triangulo valido.
#Ingrese a: 1.9
#Ingrese b: 2
#Ingrese c: 2
#El triangulo es isoceles.
#Ingrese a: 3.0
#Ingrese b: 5.0
#Ingrese c: 4.0
#El triangulo es escaleno.





# Programa para verificar si tres lados forman un triángulo válido y determinar su tipo

# Solicitar al usuario que ingrese los tres lados del triángulo
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

# Verificar si cumple la desigualdad triangular para ser un triángulo válido
if (a + b > c) and (a + c > b) and (b + c > a):
    # Si los tres lados son iguales, es un triángulo equilátero
    if a == b == c:
        print("El triangulo es equilatero.")
    # Si dos lados son iguales, es un triángulo isósceles
    elif a == b or a == c or b == c:
        print("El triangulo es isoceles.")
    # Si todos los lados son diferentes, es un triángulo escaleno
    else:
        print("El triangulo es escaleno.")
else:
    print("No es un triangulo valido.")
