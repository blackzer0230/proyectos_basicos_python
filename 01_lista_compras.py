# 2 Lista de Compras
#   Requisitos:
#    Menú interactivo con opciones: 1) Agregar, 2) Eliminar, 3) Ver lista, 4) Limpiar, 5) Salir
#    Usa while True para que el programa no termine hasta que elija "Salir"
#    La lista debe persistir mientras el programa corre


lista_compras = list(["manzanas", "peras", "limon", "putas"])


while True:

    print("\n--- LISTA DE COMPRAS ---")  # \n = salto de línea
    print("1. Agregar")
    print("2. Eliminar")
    print("3. Ver lista")
    print("4. Limpiar")
    print("5. Salir")
    
    opcion = input("elige la opcion de la lista: ")
    
    if opcion == "1":
        agregar = input("ingrese el valor que vas a ingresar: ")
        lista_compras.append(agregar)


    elif opcion == "2":
        remover = input("ingrese el valor que deseas eliminar: ")
        lista_compras.remove(remover)


    elif opcion == "3":
        for i, ii in enumerate(lista_compras, 1):
           print(f"{i}. {ii}")



    elif opcion == "4":
        lista_compras.clear()
        print("la lista se limpio por completa!!!")



    elif opcion == "5":
        print("se salio de la lista")
        break



    else:
        print("no selecionaste una opcion correcta")
