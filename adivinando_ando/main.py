# Importamos la librería 'random' para poder generar números aleatorios.
import random

# Generamos un número secreto al azar entre el 1 y el 100 (ambos inclusive) y lo guardamos.
numero = random.randint(1, 100)

# Inicializamos un contador en 0 para llevar la cuenta de cuántos intentos hace el usuario.
intentos = 0

# Mostramos un mensaje de bienvenida e instrucción en la pantalla.
print("Adivina el número entre 1 y 100")

# Iniciamos un bucle infinito (while True) que se repetirá hasta que el usuario adivine el número.
while True:
    # Pedimos al usuario que escriba un número, lo convertimos a entero (int) y lo guardamos.
    intento = int(input("Tu número: "))
    
    # Sumamos 1 al contador cada vez que el usuario introduce un número.
    intentos += 1

    # Si el número ingresado es menor que el número secreto:
    if intento < numero:
        print("Es mayor") # Le indicamos que el número oculto es más alto.
        
    # Si el número ingresado es mayor que el número secreto:
    elif intento > numero:
        print("Es menor") # Le indicamos que el número oculto es más bajo.
        
    # Si no es menor ni mayor, significa que ¡lo adivinó!
    else:
        print(f"¡Ganaste en {intentos} intentos!") # Mostramos mensaje de victoria con los intentos totales.
        break # Rompemos el bucle para que el programa termine.