inventary = {}

# Adds a new product to the inventory
def add_product():
    """
    Prompts the user for a product name, price, and quantity.
    Validates input and adds the product to the inventory if valid.
    """
    product = input("Product name: ").strip()
    if product in inventary:
        print("This product already exists.\n")
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

    inventary[product] = {"price": price, "amount_available": amount}
    print(f"Product '{product}' added successfully.\n")

# Searches for a product in the inventory
def search_p():
    """
    Prompts the user to enter a product name and displays its price and available amount.
    """
    product = input("Enter product to search: ").strip()
    bs = inventary.get(product)
    if bs:
        print(f"\nProduct: {product}\nPrice: {bs['price']}\nProducts available: {bs['amount_available']}")
    else:
        print("Product not found.\n")

# Updates the price of an existing product
def update_p():
    """
    Prompts the user to update the price of an existing product.
    """
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

# Deletes a product from the inventory
def delete_prod():
    """
    Prompts the user to delete a product from the inventory.
    Only deletes if the product exists and has available stock.
    """
    product = input("Enter the product to delete: ").strip()
    bs = inventary.get(product)
    if bs and bs['amount_available'] > 0:
        del inventary[product]
        print(f"Product '{product}' removed.\n")
    else:
        print("Product not found or unavailable.\n")

# Calculates the total value of all products in the inventory
def calc_total():
    """
    Calculates the total value of all products in the inventory by multiplying price and quantity.
    """
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
        print("There isn't a valid total.\n")

# Displays the menu of options
def display():
    """
    Displays the menu with available options for the user.
    """
    print("=== Inventory Processing ===")
    print("1. Add product")
    print("2. Search product")
    print("3. Update product")
    print("4. Delete product")
    print("5. Calculate full inventory")
    print("6. Exit")

# Main loop for handling user input and executing the selected option
while True:
    """
    Main loop where the user selects an option, and the corresponding function is executed.
    If the user selects an invalid option, an error message is shown.
    """
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


This Python script allows you to manage a product inventory. You can add products, search for products by name, update prices, delete products, and calculate the total value of the inventory. The program performs various validations to ensure that the inputs are valid.
Description
The code implements a simple system to manage a product inventory. It allows the user to perform the following actions:
• Add product: Add a new product to the inventory with its name, price, and quantity.
• Search product: Search for a product by its name and display its price and available quantity.
• Update price: Update the price of an existing product.
• Delete product: Delete a product from the inventory if it has available stock.
• Calculate total: Calculate the total value of the inventory by multiplying the price by the quantity of each product.
• Exit: End the execution of the program.
Validations
The script performs the following validations:
• Product already exists: If you try to add a product that already exists in the inventory, an error message will be displayed.
• Invalid price: If the entered price is negative, zero, or not a valid number, an error message will appear.
• Invalid quantity: If the entered quantity is negative, zero, or not a valid number, an error message will appear.
• Product not found: If you try to update or delete a product that doesn't exist, an error message will appear.