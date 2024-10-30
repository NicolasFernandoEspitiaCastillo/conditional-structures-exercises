#El joven periodista Solarrabietas debe relatar un partido de tenis, pero no conoce las reglas del deporte. En particular, no ha logrado aprender cómo saber si un set ya terminó, y quién lo ganó.

#Un partido de tenis se divide en sets. Para ganar un set, un jugador debe ganar 6 juegos, pero además debe haber ganado por lo menos dos juegos más que su rival. Si el set está empatado a 5 juegos, el ganador es el primero que llegue a 7. Si el set está empatado a 6 juegos, el set se define en un último juego, en cuyo caso el resultado final es 7-6.

#Sabiendo que el jugador A ha ganado m juegos, y el jugador B, n juegos, al periodista le gustaría saber:

#si A ganó el set, o
#si B ganó el set, o
#si el set todavía no termina, o
#si el resultado es inválido (por ejemplo, 8-6 o 7-3).
#Desarrolle un programa que solucione el problema de Solarrabietas:

#Juegos ganados por A: 4
#Juegos ganados por B: 5
#Aun no termina
#Juegos ganados por A: 5
#Juegos ganados por B: 7
#Gano B
#Juegos ganados por A: 5
#Juegos ganados por B: 6
#Aun no termina
#Juegos ganados por A: 3
#Juegos ganados por B: 7
#Invalido
#Juegos ganados por A: 6
#Juegos ganados por B: 4
#Gano A



# Programa para determinar el estado de un set de tenis

# Solicitar la cantidad de juegos ganados por A y B
juegos_A = int(input("Juegos ganados por A: "))
juegos_B = int(input("Juegos ganados por B: "))

# Verificar si el resultado es válido y determinar el estado del set
if juegos_A > 7 or juegos_B > 7:
    print("Invalido")
elif (juegos_A == 7 and juegos_B < 5) or (juegos_B == 7 and juegos_A < 5):
    print("Invalido")
elif juegos_A == 6 and juegos_B == 6:
    print("Aun no termina")
elif juegos_A == 7 and juegos_B == 6:
    print("Gano A")
elif juegos_B == 7 and juegos_A == 6:
    print("Gano B")
elif juegos_A == 6 and juegos_B <= 4:
    print("Gano A")
elif juegos_B == 6 and juegos_A <= 4:
    print("Gano B")
else:
    print("Aun no termina")
