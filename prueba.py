

inventario = {}


def añadir_producto():
    producto = input("Product name: ").strip()
    if producto in inventario:
        print("This product already exists in the catalog.\n")
        return

    precio = float(input("Price: ").strip())
    

    try:
        cantidad = int(input("Amount of product: "))
        if cantidad <= 0:
            raise ValueError
    except ValueError:
        print("Invalid number")
        return

    inventario[producto] = {
        "precio": precio,
        "cantidad_disponible": cantidad,
    }

    print(f"product '{producto}' added successfully.\n")
    
    
def buscar_p():
    producto = input("Enter product to search: ").strip()
    bs = inventario.get(producto)
    if bs:
        print(f"\nProduct: {producto}")
        print(f"Price: {bs['precio']}")
        print(f"Products availables: {bs['cantidad_disponible']}")
    else:
        print("product not found in the catalog.\n")

def editar_p():
    producto = input("Enter product to update: ").strip()
    if producto in inventario:
        nuevo_precio = float(input(f"New price for '{producto}': "))
        inventario[producto]["precio"] = nuevo_precio
        print(f"Price for '{producto}' updated to {nuevo_precio}.\n")
    else:
        print(f"Product '{producto}' not found.\n")



def eliminar_prod():
    producto = input("Enter the product to delete: ").strip()
    bs = inventario.get(producto)
    if bs:
        if bs['cantidad_disponible']>0:
            del inventario[producto]
            print(f"product '{producto}' removed from the catalog.\n")
    else:
        print("product not found in the catalog.\n")
        
        

def calc_to():
    print
    


def mostrar_menu():
    print("=== inventory processing ===")
    print("1. Add product")
    print("2. Search product")
    print("3. update product")
    print("4. Delete product")
    print("5. Calculate full inventory")
    print("6. Exit")





while True:
    mostrar_menu()
    opcion = int(input("Select an option (1-6): ").strip())
    print()
    
    if opcion == 1:
        añadir_producto()
    elif opcion==2:
        buscar_p()
    elif opcion==3:
        editar_p()
    elif opcion==4:
        eliminar_prod()
    elif opcion==5:
        calc_to()
    elif opcion==6:
        False
        
