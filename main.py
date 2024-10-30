#Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos. En caso que sea letra, determine si es mayúscula o minúscula.

#Ingrese caracter: 9
#Es numero.
#Ingrese caracter: A
#Es letra mayúscula.
#Ingrese caracter: f
#Es letra minúscula.
#Ingrese caracter: #
#No es letra ni número.#




# Programa para determinar el tipo de carácter ingresado

# Solicitar al usuario que ingrese un carácter
caracter = input("Ingrese caracter: ")

# Verificar si el carácter es una letra
if caracter.isalpha():
    if caracter.isupper():
        print("Es letra mayúscula.")
    else:
        print("Es letra minúscula.")
# Verificar si el carácter es un número
elif caracter.isdigit():
    print("Es numero.")
# Si no es ni letra ni número
else:
    print("No es letra ni número.")
