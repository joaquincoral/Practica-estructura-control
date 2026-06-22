#condicional multiple y anidada

#elif (else if) - agrega ramas intermedias

#clacificador de calificaciones

nota = float(input("calificacion (0-10): "))

if nota <0 or nota >10:
    print("Calificación inválida")
elif nota >=9.0:
    letra = "A - Excelente"
elif nota >=8.0:
    letra = "B - Bien"
elif nota >=7.0:
    letra = "c - suficiente"
elif nota >=6.0:
    letra = "D - Aprobado minimo"
else:
    letra = "F - Reprobado"

if 0 <= nota <=10:
    print(f"Nota: {nota:.1f} -> {letra}")

#Tu turno: Agrega  un mensaje que diga cuántos puntos le faltan para subir de letra. Por ejemplo, si obtuvo 7.2 (letra C), necesita 0.8 puntos para llegar a la B.

nota = 7.2  

# Validar que la nota esté en el rango correcto
if nota < 0 or nota > 10:
    print("Error: La calificación debe estar entre 0 y 10.")
else:
    # Evaluar las letras y calcular los puntos restantes
    if nota >= 9.0:
        print(f"Tu letra es A. ¡Felicidades, estás en el nivel máximo!")
    elif nota >= 8.0:
        puntos_faltantes = round(9.0 - nota, 1)
        print(f"Tu letra es B. Te faltan {puntos_faltantes} puntos para subir a la letra A.")
    elif nota >= 7.0:
        puntos_faltantes = round(8.0 - nota, 1)
        print(f"Tu letra es C. Te faltan {puntos_faltantes} puntos para subir a la letra B.")
    else:
        puntos_faltantes = round(7.0 - nota, 1)
        print(f"Tu letra es D. Te faltan {puntos_faltantes} puntos para subir a la letra C.")

#Tu turno: Reescribe el Ejercicio  usando una sola condición con and en lugar del if anidado. Luego compara las dos versiones: ¿cuál da mensajes de error más específicos y por qué?

