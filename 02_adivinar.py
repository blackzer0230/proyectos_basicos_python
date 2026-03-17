# PROYECTO #3: Adivina el Número
# Requisitos:
#    La computadora elige un número aleatorio entre 1 y 100
#    El usuario tiene intentos ilimitados (o ponle límite de 7 para más emoción)
#    Después de cada intento, dice: "Muy alto", "Muy bajo" o "¡Correcto!"
#    Al final, muestra cuántos intentos usó

import random

secreta = random.randint(1, 100)
i = 0

while True:
    i += 1
    crees = int(input("adivina el numero: "))

    if crees > secreta:
        print("muy alto!")


    elif crees < secreta:
        print("muy bajo!!")


    elif crees == secreta:
        print(f"adivinaste en {i} intentos!!! felicidades")
    
    else:
        print("ingresaste un valor incorrecto")