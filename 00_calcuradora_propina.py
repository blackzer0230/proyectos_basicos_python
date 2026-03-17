#1. Calculadora de Propinas
#    Pide el total de la cuenta, porcentaje de propina y número de personas
#    Calcula cuánto paga cada uno
#    Usa: variables, operadores, input(), f-strings
porcentaje = 10
total = input("ingrese el total de la cuenta: ")
num_personas = input("ingrese el numero de personas: ")
division = int(total) / int(num_personas)
propina = int(total) * int(porcentaje) / 100
print(f"entre los {num_personas} van a pagar ${division:.2f} y la propina sera de {propina}")