#CICLO WHILE Repite un bloque MIENTRAS una condición sea True. Se usa cuando NO sabes de antemano cuántas veces necesitas repetir el número de repeticiones depende de lo que ocurra durante la ejecución

#Regla crítica: algo dentro del while DEBE cambiar en cada iteración para que la condición eventualmente sea False. Sin eso, el ciclo nunca termina.

#Cómo mostrar un bucle infinito en clase: Escribe un while True: sin break y sin nada que cambie. Deja que el programa corra unos segundos y luego presiona Ctrl+C para interrumpirlo. El grupo necesita ver ese error en pantalla para saber qué hacer cuando les pase.

#ejercicio - while basico: contador y acumulador

N = int(input("Suma del 1 hasta: "))
i = 1 #Contador - empieza en 1
suma = 0 #Acumulador - empieza en 0

while i <= N:
    suma + suma + i
i - i +1

print(f"Suma de 1 a (N): {suma}")

#Verificación matemática: N°(N+1)/2
formula = N * (N+1) /2  #para numero entero // en vez de /
print(f"Verificación con fórmula: (formula)")

#Tu turno: Reescribe el ejercicio usando for en lugar de while. ¿Cuál versión es más natural para este problema? Explica por qué con tus palabras.

#Ejercicio - while para validar entrada: el patrón de reintento.

nota = float(input("Calificación (0-10):"))

while nota < 0 or nota > 10:
    print("Calificación inválida. Debe ser entre 8 у 10.")
    nota = float(input("Calificación (0-10)"))

print(f"Calificación registrada: {nota:.1f}")
print()

#While True + break
while True:
    edad = int(input("Tu edad (1-80):"))
    if 1 <= edad <=80:
        break
    print("Edad inválida, intenta de nuevo.")

print(f"Edad registrada: (edad)")

#Tu turno: Crea un programa que pida al usuario adivinar un número secreto (define tú el número con una constante). Con while, sigue pidiendo hasta que lo adivine e imprime cuántos intentos necesitó.

