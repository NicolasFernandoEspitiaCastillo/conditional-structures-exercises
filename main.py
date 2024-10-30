#Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento:

#Ingrese su fecha de nacimiento.
#Dia: 14
#Mes: 6
#Anno: 1948
#Usted tiene 62 annos
#Por supuesto, el resultado entregado depende del día en que su programa será ejecutado.

#Para obtener la fecha actual, puede hacerlo usando la función localtime que viene en el módulo time. Los valores se obtienen de la siguiente manera (suponiendo que hoy es 11 de marzo de 2011):

#>>> from time import localtime
#>>> t = localtime()
#>>> t.tm_mday
#11
#>>> t.tm_mon
#3
#>>> t.tm_year
#2011
#El programa debe tener en cuenta si el cumpleaños ingresado ya pasó durante este año, o si todavía no ocurre.




# Importar la función localtime para obtener la fecha actual
from time import localtime

# Solicitar la fecha de nacimiento del usuario
dia_nac = int(input("Dia: "))
mes_nac = int(input("Mes: "))
anno_nac = int(input("Anno: "))

# Obtener la fecha actual
t = localtime()
dia_actual = t.tm_mday
mes_actual = t.tm_mon
anno_actual = t.tm_year

# Calcular la edad inicial
edad = anno_actual - anno_nac

# Ajustar la edad si el cumpleaños aún no ha pasado en el año actual
if (mes_actual < mes_nac) or (mes_actual == mes_nac and dia_actual < dia_nac):
    edad -= 1

# Mostrar la edad calculada
print(f"Usted tiene {edad} annos")
