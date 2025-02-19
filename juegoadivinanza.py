import random

numero_secreto = random.randint(1,99)
print(numero_secreto)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False

print("Bienvenidx al juego de adivinar el número secreto! \nTenés 5 intentos para adivinarlo\n")

while not adivinado:
    if not cant_intentos < cant_max_intentos:
        print("GAME OVER! No pudiste adivinar el número secreto. La respuesta correcta es:",numero_secreto)
        break

    numero = int(input("Introduce un número del 1 al 99: \n"))

    if numero == numero_secreto:
        print("Felicitaciones! Adivinaste el número secreto!")
        adivinado = True
        break

    if cant_intentos <4 and numero < numero_secreto:
            print("\nEl número es mayor al ingresado")
    elif cant_intentos <4 and numero > numero_secreto:
            print("\nEl número es menor al ingresado")

    cant_intentos += 1
        
    if cant_intentos == 4:
        print("Te queda 1 intento!")

    elif cant_intentos < cant_max_intentos:
        print("Te quedan",5-cant_intentos,"intentos!")