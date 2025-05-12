# Lista predefinida de géneros válidos
generos_validos = ["Fiction", "Non-Fiction", "Science", "Biography", "Children"]

# Estructura de la biblioteca (diccionario de libros)
biblioteca = {}

# Función 1: Añadir libros
def añadir_libro():
    titulo = input("Book title: ").strip()
    if titulo in biblioteca:
        print("This book already exists in the catalog.\n")
        return

    autor = input("Author: ").strip()
    genero = input(f"Genre ({', '.join(generos_validos)}): ").strip()

    if genero not in generos_validos:
        print("Invalid genre. Book not added.\n")
        return

    try:
        copias = int(input("Number of copies: "))
        if copias <= 0:
            raise ValueError
    except ValueError:
        print("Invalid number of copies. Book not added.\n")
        return

    biblioteca[titulo] = {
        "autor": autor,
        "genero": genero,
        "copias_disponibles": copias,
        "copias_totales": copias
    }

    print(f"Book '{titulo}' added successfully.\n")

# Función 2: Buscar libro por título
def buscar_libro():
    titulo = input("Enter the book title to search: ").strip()
    libro = biblioteca.get(titulo)
    if libro:
        print(f"\nTitle: {titulo}")
        print(f"Author: {libro['autor']}")
        print(f"Genre: {libro['genero']}")
        print(f"Available copies: {libro['copias_disponibles']}/{libro['copias_totales']}\n")
    else:
        print("Book not found in the library.\n")

# Función 3: Registrar préstamo
def prestar_libro():
    titulo = input("Enter the book title to lend: ").strip()
    libro = biblioteca.get(titulo)
    if libro:
        if libro["copias_disponibles"] > 0:
            libro["copias_disponibles"] -= 1
            print(f"Book '{titulo}' has been lent.\n")
        else:
            print("No available copies for this book.\n")
    else:
        print("Book not found in the library.\n")

# Función 4: Registrar devolución
def devolver_libro():
    titulo = input("Enter the book title to return: ").strip()
    libro = biblioteca.get(titulo)
    if libro:
        if libro["copias_disponibles"] < libro["copias_totales"]:
            libro["copias_disponibles"] += 1
            print(f"Book '{titulo}' has been returned.\n")
        else:
            print("All copies are already in the library.\n")
    else:
        print("Book not found in the library.\n")

# Función 5: Eliminar libro
def eliminar_libro():
    titulo = input("Enter the book title to delete: ").strip()
    libro = biblioteca.get(titulo)
    if libro:
        if libro["copias_disponibles"] == libro["copias_totales"]:
            del biblioteca[titulo]
            print(f"Book '{titulo}' removed from the catalog.\n")
        else:
            print("Cannot delete book. Some copies are still lent out.\n")
    else:
        print("Book not found in the library.\n")

# Función 6: Listar por género
def listar_por_genero():
    genero = input(f"Enter genre ({', '.join(generos_validos)}): ").strip()
    if genero not in generos_validos:
        print("Invalid genre.\n")
        return

    encontrados = [titulo for titulo, datos in biblioteca.items() if datos["genero"] == genero]

    if encontrados:
        print(f"\nBooks in genre '{genero}':")
        for titulo in encontrados:
            datos = biblioteca[titulo]
            print(f"- {titulo} by {datos['autor']} ({datos['copias_disponibles']} available)")
        print()
    else:
        print(f"No books found in genre '{genero}'.\n")

# Función 7: Resumen de inventario
def resumen_inventario():
    total_libros = len(biblioteca)
    total_copias = sum(libro["copias_totales"] for libro in biblioteca.values())
    copias_disponibles = sum(libro["copias_disponibles"] for libro in biblioteca.values())

    print("\n=== Inventory Summary ===")
    print(f"Total unique books: {total_libros}")
    print(f"Total copies: {total_copias}")
    print(f"Total available copies: {copias_disponibles}\n")

# Menú principal
def mostrar_menu():
    print("=== Community Library System ===")
    print("1. Add new book")
    print("2. Search book by title")
    print("3. Lend book")
    print("4. Return book")
    print("5. Delete book")
    print("6. List books by genre")
    print("7. Show inventory summary")
    print("8. Exit")

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Select an option (1-8): ").strip()
    print()

    if opcion == "1":
        añadir_libro()
    elif opcion == "2":
        buscar_libro()
    elif opcion == "3":
        prestar_libro()
    elif opcion == "4":
        devolver_libro()
    elif opcion == "5":
        eliminar_libro()
    elif opcion == "6":
        listar_por_genero()
    elif opcion == "7":
        resumen_inventario()
    elif opcion == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.\n")