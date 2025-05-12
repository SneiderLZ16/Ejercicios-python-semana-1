inventary = {}

# method to add product
def add_product():
    product = input("Product name: ").strip()
    if product in inventary:
        print("This product already exists in the catalog.\n")
        return

    try:
        price = float(input("Price: ").strip())
        if price <= 0:
            raise ValueError
    except ValueError:
        print("Invalid price")
        return

    try:
        amount = int(input("Amount of product: "))
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Invalid number")
        return

    inventary[product] = {
        "price": price,
        "amount_available": amount,
    }

    print(f"Product '{product}' added successfully.\n")

# method to search for product
def search_p():
    product = input("Enter product to search: ").strip()
    bs = inventary.get(product)
    if bs:
        print(f"\nProduct: {product}")
        print(f"Price: {bs['price']}")
        print(f"Products available: {bs['amount_available']}")
    else:
        print("Product not found in the catalog.\n")

# method to update price
def update_p():
    product = input("Enter product to update: ").strip()
    if product in inventary:
        try:
            new_price = float(input(f"New price for '{product}': "))
            if new_price <= 0:
                raise ValueError
        except ValueError:
            print("Invalid value")
            return
        inventary[product]["price"] = new_price
        print(f"Price for '{product}' updated to {new_price}.\n")
    else:
        print(f"Product '{product}' not found.\n")

# method to delete record
def delete_prod():
    product = input("Enter the product to delete: ").strip()
    bs = inventary.get(product)
    if bs:
        if bs['amount_available'] > 0:
            del inventary[product]
            print(f"Product '{product}' removed from the catalog.\n")
    else:
        print("Product not found in the catalog.\n")

# method to calculate total inventory value
def calc_total():
    smt = 0
    try:
        for product in inventary:
            total = inventary[product]["price"]
            cn = inventary[product]["amount_available"]
            sm = total * cn
            if sm <= 0:
                raise ValueError
            smt += sm
        print(f"Your net total is: {smt}")
    except ValueError:
        print("There isn't current net.")

# Method to display options
def display():
    print("=== Inventory Processing ===")
    print("1. Add product")
    print("2. Search product")
    print("3. Update product")
    print("4. Delete product")
    print("5. Calculate full inventory")
    print("6. Exit")

# main loop
while True:
    try:
        display()
        option = int(input("Select an option (1-6): ").strip())
        print()
        if option == 1:
            add_product()
        elif option == 2:
            search_p()
        elif option == 3:
            update_p()
        elif option == 4:
            delete_prod()
        elif option == 5:
            calc_total()
        elif option == 6:
            print("Exiting the program.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid option (1-6).")
