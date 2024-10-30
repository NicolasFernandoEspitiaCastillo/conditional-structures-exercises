#Cuando la Tierra completa una órbita alrededor del Sol, no han transcurrido exactamente 365 rotaciones sobre sí misma, sino un poco más. Más precisamente, la diferencia es de más o menos un cuarto de día.

#Para evitar que las estaciones se desfasen con el calendario, el calendario juliano introdujo la regla de introducir un día adicional en los años divisibles por 4 (llamados bisiestos), para tomar en consideración los cuatro cuartos de día acumulados.

#Sin embargo, bajo esta regla sigue habiendo un desfase, que es de aproximadamente 3/400 de día.

#Para corregir este desfase, en el año 1582 el papa Gregorio XIII introdujo un nuevo calendario, en el que el último año de cada siglo dejaba de ser bisiesto, a no ser que fuera divisible por 400.

#Escriba un programa que indique si un año es bisiesto o no, teniendo en cuenta cuál era el calendario vigente en ese año:

#Ingrese un anno: 1988
#1988 es bisiesto
#Ingrese un anno: 2011
#2011 no es bisiesto
#Ingrese un anno: 1700
#1700 no es bisiesto
#Ingrese un anno: 1500
#1500 es bisiesto
#Ingrese un anno: 2400
#2400 es bisiesto



# Programa para determinar si un año es bisiesto

# Solicitar al usuario que ingrese un año
anno = int(input("Ingrese un anno: "))

# Verificar si el año es bisiesto según el calendario correspondiente
if anno < 1582:
    # Regla del calendario juliano: años divisibles por 4 son bisiestos
    if anno % 4 == 0:
        print(f"{anno} es bisiesto")
    else:
        print(f"{anno} no es bisiesto")
else:
    # Regla del calendario gregoriano
    if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
        print(f"{anno} es bisiesto")
    else:
        print(f"{anno} no es bisiesto")
