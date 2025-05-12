# Lista para guardar los contactos
agenda = []

# Función para agregar un contacto
def agregar_contacto():
    nombre = input("Nombre del contacto: ")
    telefono = input("Teléfono: ")
    contacto = {"nombre": nombre, "telefono": telefono}
    agenda.append(contacto)
    print(f"Contacto '{nombre}' agregado.\n")

# Función para mostrar todos los contactos
def mostrar_agenda():
    if not agenda:
        print("La agenda está vacía.\n")
    else:
        print("Agenda de contactos:")
        for i, contacto in enumerate(agenda, start=1):
            print(f"{i}. Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}")
        print()

# Función para eliminar un contacto
def eliminar_contacto():
    nombre = input("Nombre del contacto a eliminar: ")
    for contacto in agenda:
        if contacto["nombre"] == nombre:
            agenda.remove(contacto)
            print(f"Contacto '{nombre}' eliminado.\n")
            return
    print(f"Contacto '{nombre}' no encontrado.\n")

# Función para editar un contacto
def editar_contacto():
    nombre = input("Nombre del contacto a editar: ")
    for contacto in agenda:
        if contacto["nombre"] == nombre:
            nuevo_nombre = input(f"Nuevo nombre (deja vacío para mantener '{nombre}'): ")
            nuevo_telefono = input(f"Nuevo teléfono (deja vacío para mantener '{contacto['telefono']}'): ")
            
            if nuevo_nombre:
                contacto["nombre"] = nuevo_nombre
            if nuevo_telefono:
                contacto["telefono"] = nuevo_telefono

            print("Contacto actualizado.\n")
            return
    print(f"Contacto '{nombre}' no encontrado.\n")

# Función para mostrar el menú
def mostrar_menu():
    print("=== Agenda de Contactos ===")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Eliminar contacto")
    print("4. Editar contacto")
    print("5. Salir")

# Programa principal con bucle
while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-5): ")
    print()

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        mostrar_agenda()
    elif opcion == "3":
        eliminar_contacto()
    elif opcion == "4":
        editar_contacto()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.\n")