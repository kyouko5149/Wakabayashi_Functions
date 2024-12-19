
burger_menu = {
    "Massive Cheese Burger" : 150.00,
    "Mushroom Burger"  : 130.00,
    "Bacon Burger" : 100.00,
    "Turkey Burger" : 130.00
}

meal_menu = {
    "Fish Fillet" : 120.00,
    "Tuna Steak" : 170.00,
    "Egg with toast" : 100.00,
    "Pork Chop Tonkatsu" : 180.00,
    "Stewed Beef" : 160.00
}

def menu():
    print("\t MENU \t")
    print("\n\t BURGER MENU \t")
    for burger, price in burger_menu.items():
        print(f"{burger}: ₱{price:.2f}")
    print("\n\t MEALS \t")
    for item, price in meal_menu.items():
        print(f"{item}: ₱{price:.2f}")

def order():
    orders = {}
    print("\nMAKE SURE TO WRITE THE EXACT WORDS\nEnter 'done' when you're finish ordering.. \n ")
    while True:
        user_order = input("Enter your orders: ").strip()
        
        if user_order.lower() == "done":
            break

        if user_order in burger_menu or user_order in meal_menu:
            try:
                quantity = int(input(f"How many order for {user_order}: "))
                if quantity < 1:
                    print("We only accept more than 1.")
                    continue
                if user_order in orders:
                    orders[user_order] += quantity
                else:
                    orders[user_order] = quantity
            
            except ValueError:
                print("Enter valid number for quantity!")
        else:
            print(f"Sorry, {user_order} is not in our menu.")

    return orders

def total_payment(orders):
    total = 0 
    print("\n\t Total Receipt \t\n")

    overall_menu = {**burger_menu, **meal_menu}

    for item, quantity in orders.items():
        if item in overall_menu:
            price = overall_menu[item]
            cost = price * quantity
            total += cost
            print(f"{item} x{quantity}: ₱{cost:.2f}")

    print(f"\nTotal: ₱{total:.2f}") 
    return total


def payment(total):
    while True:
        try:
            cash = float(input("\nPlease enter cash: "))
            if cash >= total:
                change = cash - total
                print(f"Payment Done! Your change is ₱{change:.2f}.")
                break
            else:
                print("Insufficient cash. Please pay exact or higher amount.")

        except ValueError:
            print("Enter valid cash/number!")


menu()

user_orders = order()

if user_orders:
    total = total_payment(user_orders)
    payment(total)
else:
    print("Bye..")






