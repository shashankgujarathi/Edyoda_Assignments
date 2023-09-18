import random

# Sample data (for demonstration purposes)
food_items = [
    {"FoodID": 1, "Name": "Tandoori Chicken", "Quantity": "4 pieces", "Price": 240, "Discount": 0, "Stock": 50},
    {"FoodID": 2, "Name": "Vegan Burger", "Quantity": "1 piece", "Price": 320, "Discount": 10, "Stock": 30},
    {"FoodID": 3, "Name": "Truffle Cake", "Quantity": "500gm", "Price": 900, "Discount": 5, "Stock": 20},
]

users = []  # Store user data (for demonstration purposes)

# Admin functions
def add_food_item():
    food_id = len(food_items) + 1
    name = input("Enter food item name: ")
    quantity = input("Enter quantity (e.g., 100ml, 250gm, 4 pieces): ")
    price = float(input("Enter price: "))
    discount = float(input("Enter discount (%): "))
    stock = int(input("Enter stock quantity: "))
    food_item = {"FoodID": food_id, "Name": name, "Quantity": quantity, "Price": price, "Discount": discount, "Stock": stock}
    food_items.append(food_item)
    print(f"Food item '{name}' added successfully.")

def edit_food_item():
    food_id = int(input("Enter FoodID to edit: "))
    for item in food_items:
        if item["FoodID"] == food_id:
            print("Current Food Item Details:")
            print(f"Name: {item['Name']}")
            print(f"Quantity: {item['Quantity']}")
            print(f"Price: {item['Price']}")
            print(f"Discount: {item['Discount']}%")
            print(f"Stock: {item['Stock']}")
            name = input("Enter new food item name (leave empty to keep current): ")
            quantity = input("Enter new quantity (leave empty to keep current): ")
            price = input("Enter new price (leave empty to keep current): ")
            discount = input("Enter new discount (leave empty to keep current): ")
            stock = input("Enter new stock quantity (leave empty to keep current): ")
            if name:
                item["Name"] = name
            if quantity:
                item["Quantity"] = quantity
            if price:
                item["Price"] = float(price)
            if discount:
                item["Discount"] = float(discount)
            if stock:
                item["Stock"] = int(stock)
            print(f"Food item with FoodID {food_id} updated successfully.")
            break
    else:
        print(f"Food item with FoodID {food_id} not found.")

def view_food_items():
    print("List of Food Items:")
    for item in food_items:
        print(f"FoodID: {item['FoodID']}")
        print(f"Name: {item['Name']}")
        print(f"Quantity: {item['Quantity']}")
        print(f"Price: {item['Price']}")
        print(f"Discount: {item['Discount']}%")
        print(f"Stock: {item['Stock']}")
        print()

def remove_food_item():
    food_id = int(input("Enter FoodID to remove: "))
    for item in food_items:
        if item["FoodID"] == food_id:
            food_items.remove(item)
            print(f"Food item with FoodID {food_id} removed successfully.")
            break
    else:
        print(f"Food item with FoodID {food_id} not found.")

# User functions
def user_registration():
    full_name = input("Enter your Full Name: ")
    phone_number = input("Enter your Phone Number: ")
    email = input("Enter your Email: ")
    address = input("Enter your Address: ")
    password = input("Create a Password: ")
    user = {"Full Name": full_name, "Phone Number": phone_number, "Email": email, "Address": address, "Password": password}
    users.append(user)
    print("User registration successful.")

def user_login():
    email = input("Enter your Email: ")
    password = input("Enter your Password: ")
    for user in users:
        if user["Email"] == email and user["Password"] == password:
            print("User login successful.")
            return
    print("Invalid credentials. Please try again.")

def place_order():
    if not food_items:
        print("No food items available.")
        return
    print("List of Food Items:")
    for item in food_items:
        print(f"FoodID: {item['FoodID']}, Name: {item['Name']}, Quantity: {item['Quantity']}, Price: {item['Price']}")
    user_input = input("Enter the FoodIDs you want to order (e.g., 1 2 3): ").split()
    order_items = []
    total_price = 0
    for food_id in user_input:
        food_id = int(food_id)
        for item in food_items:
            if item["FoodID"] == food_id:
                order_items.append(item)
                total_price += item["Price"]
                break
    print("Selected Food Items:")
    for item in order_items:
        print(f"Name: {item['Name']}, Quantity: {item['Quantity']}, Price: {item['Price']}")
    print(f"Total Price: {total_price}")

def main():
    while True:
        print("\n----------------- Food Ordering App -----------------")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print("\n----------------- Admin Menu -----------------")
            print("1. Add new food item")
            print("2. Edit food item")
            print("3. View list of all food items")
            print("4. Remove a food item")
            print("5. Back to main menu")
            admin_choice = input("Enter your choice: ")
            if admin_choice == '1':
                add_food_item()
            elif admin_choice == '2':
                edit_food_item()
            elif admin_choice == '3':
                view_food_items()
            elif admin_choice == '4':
                remove_food_item()
            elif admin_choice == '5':
                continue
        elif choice == '2':
            print("\n----------------- User Menu -----------------")
            print("1. Register")
            print("2. Login")
            print("3. Place New Order")
            print("4. Exit")
            user_choice = input("Enter your choice: ")
            if user_choice == '1':
                user_registration()
            elif user_choice == '2':
                user_login()
            elif user_choice == '3':
                place_order()
            elif user_choice == '4':
                continue
        elif choice == '3':
            print("Goodbye!")
            break

if __name__ == '__main__':
    main()
