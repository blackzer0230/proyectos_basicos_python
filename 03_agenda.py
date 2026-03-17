# PROYECTO 4: Agenda de Contactos (Diccionarios)
# Requisitos:

#     Menú: 1) Agregar, 2) Buscar, 3) Eliminar, 4) Listar todos, 5) Salir
#     Cada contacto: nombre (clave), teléfono, email (valores en diccionario anidado)
#     Usa diccionarios 


agenda = {
    "harry": {"telef": "000-0000", "email": "harry@gamil.com"},
    "sthefanny": {"telef": "000-0001", "email": "tefy@gmail.com"}
}

while True:
    # presentacion de las opciones de la agenda
    print("\n---AGENDA---")
    print("1 - agregar contactos")
    print("2 - buscar contactos")
    print("3 - eliminar contactos")
    print("4 - ver todos")
    print("5 - salir")
    eleccion = input("----> ") # elecion de opcion!! 




            # agregar 
    if eleccion == "1":
        nombre_agregar = input("ingrese el nombre: ")
        telefono_agregar = input("ingrese el telefono: ")
        email_agregar = input("ingrese el email: ")

        # update para agregar usuarios a la agenda
            #este metodo no sabia que podia funcionar para agregar muchas mas opciones
        agenda.update({
            nombre_agregar: {"telef": telefono_agregar, "email": email_agregar}
        })




            # buscar
    elif eleccion == "2":
        nombre_buscar = input("----> ")
        contacto = agenda.get(nombre_buscar)
        if contacto:
            print(f"{nombre_buscar} - {contacto["telef"]} - {contacto["email"]}")

        else:
            print("no existe")

 


    # eliminar
    elif eleccion == "3":
        nombre_del = input("----> ")
        if nombre_del in agenda:
            del agenda[nombre_del]
            print(f"{nombre_del} eliminado de la lista")
        else:
            print("no se encontro en la agenda3")


    
    # listar todos
    elif eleccion == "4":
        for nombre, info in sorted(agenda.items()):
            print(f"{nombre} - celeular {info["telef"]} - email {info["email"]}")
    
    
    
    
    
    
    
    
    # salir 
    elif eleccion == "5":
        print("elegiste salir")
        break
    
    else:
        print("seguro que elegiste una opcion incorrecta")
