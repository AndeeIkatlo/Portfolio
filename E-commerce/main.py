import os  # Import the os module to clear the screen

products = []
product_id_counter = 1
def add_products(name, price, quantity):
    global product_id_counter
    new_product = {
        "id": product_id_counter,
        "name": name,
        "price": price,
        "quantity": quantity
    }
    products.append(new_product)
    product_id_counter += 1
    print("Added product successfully!")
    input("Press Enter to continue...")
    clear_screen()
    show_menu()

def view_products():
    if not products:
        print("No products to view.")
    else:
        print("\nAll Products:")
        for product in products:
            print(f"Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")
    input("Press Enter to continue...")
    clear_screen()
    show_menu()

def update_products(product_name, new_price, new_quantity):
    for product in products:
        if product["name"] == product_name:
            product["price"] = new_price
            product["quantity"] = new_quantity
            print("Product updated successfully!")
            break
    else:
        print("Product name not found.")
    input("Press Enter to continue...")
    clear_screen()
    show_menu()

def delete_products():
    if not products:
        print("No products to delete.")
        input("Press Enter to continue...")
        clear_screen()
        show_menu()
        return
    
    print("\nAll Products: ")
    for product in products:
        print(f"ID: {product['id']} | Name: {product['name']} | Price: {product['price']} | Quantity: {product['quantity']}")

    while True:
        product_id_input = input("Enter the ID of the product to delete: ")
        if product_id_input.isdigit():
            product_id = int(product_id_input)
            if any(product['id'] == product_id for product in products):
                for product in products:
                    if product['id'] == product_id:
                        products.remove(product)
                        print("Product deleted successfully!")
                        input("Press Enter to continue...")
                        clear_screen()
                        show_menu()
                        return
            else:
                print("Product ID not found. Please enter a valid product ID.")
        else:
            print("Invalid input. Please enter a valid product ID.")




def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen based on the operating system

def show_menu():
    print("_"*23)
    print("|PRODUCTS APPLICATION   |")
    print("|","_"*21,"|")
    print("|1. Add a product       |")
    print("|2. View all products   |")
    print("|3. Update products     |")
    print("|4. Delete products     |")
    print("|5. Exit                |")
    print("-" * 24) 
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        add_products(name, price, quantity)
    elif choice == '2':
        view_products()
    elif choice == '3':
        product_name = input("Enter the product name: ")
        new_price = float(input("Enter the new price: "))
        new_quantity = int(input("Enter the new quantity: "))
        update_products(product_name, new_price, new_quantity)
    elif choice == '4':
        delete_products()
    elif choice == '5':
        print("Thank you for using the application.")
        exit()

def main():
    clear_screen()
    show_menu()

if __name__ == "__main__":
    main()
