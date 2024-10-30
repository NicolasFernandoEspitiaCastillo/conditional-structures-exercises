#Escriba un programa que simule una calculadora básica, este puede realizar operación de suma, resta, multiplicación y división.

#El programa debe recibir como entrada 2 números reales y un operador, que puede ser +, -, * o /.

#La salida del programa debe ser el resultado de la operación.

#Operando: 3
#Operador: +
#Operando: 2
#3 + 2 = 5
#Operando: 6
#Operador: -
#Operando: 7
#6 - 7 = -1
#Operando: 4
#Operador: *
#Operando: 5
#4 * 5 = 20
#Operando: 10
#Operador: /
#Operando: 4
#10 / 4 = 2.5
#Operando: -1
#Operador: **
#Operando: 4
#-1 ** 4 = 1





# Programa para una calculadora básica

# Solicitar el primer operando
operando1 = float(input("Operando: "))
# Solicitar el operador
operador = input("Operador: ")
# Solicitar el segundo operando
operando2 = float(input("Operando: "))

# Inicializar la variable para el resultado
resultado = None

# Realizar la operación según el operador ingresado
if operador == '+':
    resultado = operando1 + operando2
elif operador == '-':
    resultado = operando1 - operando2
elif operador == '*':
    resultado = operando1 * operando2
elif operador == '/':
    if operando2 != 0:
        resultado = operando1 / operando2
    else:
        print("Error: División por cero.")
elif operador == '**':
    resultado = operando1 ** operando2
else:
    print("Operador no válido.")

# Mostrar el resultado si la operación fue válida
if resultado is not None:
    print(f"{operando1} {operador} {operando2} = {resultado}")
