# Python usa la sangria (espacios al inicio de la linea) para delimitar bloques de codigo.{}, Python usa 4 espacios por nivel. Esta es la diferencia visual mas importante entre python y otros lenguajes.

#if condicion:
#  instruccion1
#else:
#  instruccion2

#Toda linea de control termina su primera linea con dos puntos ":". Los dos puntos le dicen python: el bloque de esta estructura comienza en la siguiente linea. Si se omiten, Python genera SyntaxError: expected ':'

#= asignar un valor
#== comparar dos valores igual que
#!= Diferente de
#> Mayor que / >= Mayor o igual
#< Menor que / <= Menor o igual
# and Ambas condiciones True / or Al menos una es true / not Negacion logica
#IF ejecuta un bloque unicamente si la condicion es TRUE. Si la condicion es falsa, el bloque se salta por completo y el programa continua. Solo tiene una rama posible.

#SI condicion ENTONCES
# instruccion
#FIN SI
    # SI FALSE -> Se omite el bloque

nota = 8.5

if nota >=6.0:
    print("EL ALUMNO APROBO")

print("FIN DEL PROGRAMA")





#CONDICIONAL DOBLE - IF/ELSE
#El else garantiza que SIEMPRE se ejecuta algo. Sin importar si la condición es True o False, el programa toma uno de los dos caminos. Nunca quedan casos sin respuesta.

#EJERCICIO 2

CALIFICACION_MINIMA = 7.0

nota = float(input("Ingresa tu calificacion"))

if nota >= CALIFICACION_MINIMA:
    print(f"Aprobando con {nota:.1f}")
else:
    print(f"Reprobado con {nota:.1f}")
    faltaron = CALIFICACION_MINIMA - nota
    print(f"Te faltaron {faltaron:.1f} puntos para aprobar")

#Condiciones compuestas: and / or en accion

edad = int(input("Tu edad: "))
tienes_ine = input("¿Tienes INE (si/no): ")

if edad >= 18 and tienes_ine == "si":
    print("Puedes votar")
else:
    print("No puedes votar aun")


#Valoracion de rango con 'and' y 'or'
calificacion = float(input("calificacion (0-10) "))

if calificacion <0 or calificacion >10:
    print("calificacion fuera de rango")
else:
    print(f"calificacion registrada: {calificacion:.1f}")

#Tu turno: Crea una condición que verifique si un año es bisiesto. Un año es bisiesto si es divisible entre 4, Y si es divisible entre 100, también debe ser divisible entre 400. Pista: usa el operador % (módulo).

año = 2024  

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"¡El año {año} es bisiesto! (si)")
else:
    print(f"El año {año} no es bisiesto. (no)")

