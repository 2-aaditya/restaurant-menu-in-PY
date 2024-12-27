menu = {
    'pizza': 40,
    'pasta': 30,
    'burger': 20,
    'colddrink': 100,
}

print("Welcome to our restaurant!")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

order_total = 0

while True:
    item = input("Enter your food item: ")
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to your order.")
    else:
        print(f"Ordered item {item} is not available!")

    another_order = input("Do you want to add another item? (yes/no): ")
    if another_order.lower() != "yes":
        break

print(f"The total amount of your order is Rs{order_total}")