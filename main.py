#El riesgo de que una persona sufra enfermedades coronarias depende de su edad y su índice de masa corporal:

 	#edad < 45	edad ≥ 45
#IMC < 22.0	bajo	medio
#IMC ≥ 22.0	medio	alto
#El índice de masa corporal es el cuociente entre el peso del individuo en kilos y el cuadrado de su estatura en metros.

#Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona, y le entregue su condición de riesgo.



# Programa para calcular el riesgo de enfermedades coronarias

# Solicitar al usuario su estatura en metros, peso en kilos y edad
estatura = float(input("Ingrese su estatura en metros: "))
peso = float(input("Ingrese su peso en kilos: "))
edad = int(input("Ingrese su edad en años: "))

# Calcular el índice de masa corporal (IMC)
imc = peso / (estatura ** 2)

# Determinar el nivel de riesgo basado en IMC y edad
if edad < 45:
    if imc < 22.0:
        riesgo = "bajo"
    else:
        riesgo = "medio"
else:
    if imc < 22.0:
        riesgo = "medio"
    else:
        riesgo = "alto"

# Mostrar el resultado del riesgo
print(f"Su condición de riesgo es: {riesgo}")
