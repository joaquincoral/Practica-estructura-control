#CICLO FOR //Repite un bloque para cada elemento de una secuencia. Se usa cuando sabes de antemano cuántas veces repetir o cuando quieres recorrer los elementos de una lista, rango o cadena.

#Ejercicio: Variante de range()
#range(fin) - empieza en 0, termina antes del fin
print("range(5)")
for i in range(5):
    print(i, end=" ") #0 1 2 3 4
print()

#range (inicio, fin) - desde inicio hasta fin
print("range(1,6):")
for i in range(1, 6):
    print(i, end= "") #12
print()

#range(inicio, fin, paso) paso personalizado
print("Pares del e al 10:")
for i in range(0, 11, 2):
    print(i, end="")
print()

# Cuenta regresiva con paso negativo
print("Cuenta regresiva:")
for i in range(5, 0, -1):
    print(i, end=" ")
print("[Despegue")

#Tu turno: Escribe un for que imprima solo los múltiplos de 3 entre 3 y 30 usando range() con los argumentos correctos. No uses if dentro del for para filtrar — usa el paso de range().
print("RANGO DE 3 A 33 ")
for i in range(3, 31, 3):
    print(i, end= " ")
print()

#Ejercicio - for recorriendo una lista: promedio y conteo.
#El for no solo funciona con números. Puede recorrer cualquier y acumular

calificaciones = [8.5, 9.0, 6.5, 10.0, 7.5, 5.0, 8.0]

print("Calificaciones del grupo:")

for calificacion in calificaciones:
    print(f" {calificacion :.1f}")

total = 0
aprobados = 0

for calificacion in calificaciones:
    total = total + calificacion
    if calificacion >= 6.0:
        aprobados = aprobados + 1

promedio = total / len(calificaciones)
reprobados = len(calificaciones) - aprobados

print(f"\nPromedio del grupo: {promedio :.2f}")
print(f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")

#Turno: encuentra e imprime la calificación más alta y la más baja. Necesitarás dos variables que guarden el máximo y el mínimo mientras recorres la lista.

calificaciones = [8.5, 9.0, 6.5, 10.0, 7.5, 5.0, 8.0]

print("Calificaciones del grupo:")

for calificacion in calificaciones:
    print(f" {calificacion :.1f}")

total = 0
aprobados = 0

max_cal = calificacion [0]
min_cal = calificacion [0]

for calificacion in calificaciones:
    total = total + calificacion
    if calificacion >= 6.0:
        aprobados = aprobados + 1
    if calificacion> max_cal:
        max_cal = calificacion
    if calificacion < min_cal:
        min_cal = calificacion

promedio = total / len(calificaciones)
reprobados = len(calificaciones) - aprobados

print(f"\nPromedio del grupo: {promedio :.2f}")
print(f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")
print(f"La calificación más alta es: {max_cal}")
print(f"La calificación más baja es: {min_cal}")

#Ejercicio: for con enumarate(): índice y valor juntos.
#enumerate() te da la posición y el valor en cada iteración. Múy útil para reportes numerados.

alumnos = ["Iran", "Povedano", "Gissel", "Susana", "Zeus", "Carlos", "Sulub"]
notas = [9.0, 7.5, 8.0, 9.5, 6.0, 10.0, 9.8]

#encabezado de la tabla
print(f"{'No.' :<5} {'Alumno' :<12} {'Nota':>6} {'Estado' :< 10}")
print("-"*37)

for i, alumno in enumerate(alumnos):
    nota = notas[i]
    estado = "Aprobado" if nota >= 7.0 else "Reprobado"
    print(f"{i+1 :< 5} {alumno :< 12} {nota:>6.1f} {estado :< 10}")

#Turno: Agrega al ejercicio un resumen al final del reporte: promedio del grupo y cantidad de aprobados, calculados dentro del mismo for que genera el reporte.

lista_alumnos = [
    {"nombre": "Ana", "nota": 9.5},
    {"nombre": "Luis", "nota": 7.0},
    {"nombre": "Sofia", "nota": 8.5},
    {"nombre": "Carlos", "nota": 5.0},
    {"nombre": "Valentina", "nota": 10.0}
]

suma_notas = 0
cantidad_aprobados = 0
total_alumnos = len(lista_alumnos)

mejor_nota = -1
peor_nota = 11
mejor_alumno = ""
peor_alumno = ""

print("=== Registro de calificaciones ===")
print("(captura de datos...)\n")

print("=== Reporte Final ===")

print("Alumno\t\tNota\tEstado\t\tLetra")
print("-" * 50)

for alumno in lista_alumnos:
    nota_final = alumno['nota']
    nombre = alumno['nombre']
    
    if nota_final >= 6.0:  
        estado = "Aprobado"
        cantidad_aprobados += 1
    else:
        estado = "Reprobado"
        
    if nota_final >= 9.0:   letra = "A"
    elif nota_final >= 8.0: letra = "B"
    elif nota_final >= 7.0: letra = "C"
    else:                   letra = "F"
    
    print(f"{nombre:<15}{nota_final:<8.1f}{estado:<16}{letra}")
    
    suma_notas += nota_final
    
    if nota_final > mejor_nota:
        mejor_nota = nota_final
        mejor_alumno = nombre
    if nota_final < peor_nota:
        peor_nota = nota_final
        peor_alumno = nombre

print("-" * 50)

if total_alumnos > 0:
    promedio_grupo = suma_notas / total_alumnos
    cantidad_reprobados = total_alumnos - cantidad_aprobados
    porcentaje_aprobados = (cantidad_aprobados / total_alumnos) * 180 # Espera, la fórmula correcta es * 100 para porcentaje.
    porcentaje_aprobados = (cantidad_aprobados / total_alumnos) * 100
    
    print(f"Promedio:\t{promedio_grupo:.2f}")
    print(f"Aprobados:\t{cantidad_aprobados}  |  Reprobados: {cantidad_reprobados}")
    print("-" * 50)
    print(f"Mejor calificación:\t{mejor_alumno} con {mejor_nota:.1f}")
    print(f"Peor calificación:\t{peor_alumno} con {peor_nota:.1f}")
    print(f"Porcentaje de aprobación:\t{porcentaje_aprobados:.1f}%")