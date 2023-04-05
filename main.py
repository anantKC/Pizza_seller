#Pizza Names
# Veggie Pizza. ...
# Pepperoni Pizza
# Meat Pizza
# Margherita Pizza
# BBQ Chicken Pizza
# Hawaiian Pizza
# Buffalo Pizza

#Pizza Topings
# Pepperoni.
# Mushroom.
# Extra cheese.
# Sausage.
# Onion.
# Black olives.
# Green pepper.

list_of_pizza_names ={
    1:'Veggie Pizza',
    2:'Pepperoni Pizza',
    3:'Meat Pizza',
    4:'Margherita Pizza',
    5:'BBQ Chicken Pizza',
}

list_of_topping_names ={
    1:'Pepperoni',
    2:'Mushrooms',
    3:'Extra cheese',
    4:'Sausage',
    5:'Onion',
}

pizza_available_at_store = {
    'Veggie Pizza': 150,
    'Pepperoni Pizza': 180,
    'Meat Pizza': 200,
    'Margherita Pizza': 210,
    'BBQ Chicken Pizza': 240
}

pizza_topings_available_at_store = {
    'Pepperoni': 45,
    'Mushrooms': 20,
    'Extra cheese': 60,
    'Sausage':50,
    'Onion': 15,
}

selected_pizza = []
selected_toppings = []

def select_pizza():
    print("Please select the pizza available at the store")
    for pizza, price in pizza_available_at_store.items():
        print(f"{pizza} - Rs{price}")
    pizza_name = input("Select your choice of pizza ")
    while pizza_name not in pizza_available_at_store:
        print("Invalid choice, please type again")
        pizza_name = input("Please select your choice of pizza again ")
    if pizza_name in pizza_available_at_store:
        selected_pizza.append(pizza_name)
        print(f"{pizza_name}  placed in your order")

def select_toppings():
    print("Please select the pizza toppings available at the store")
    for topping, price in pizza_topings_available_at_store.items():
        print(f"{topping} - Rs{price}")
    topping_name = input("Select your choice of topping or enter 'no' to finish ")
    while topping_name not in pizza_topings_available_at_store and topping_name != 'no':
        print("Invalid choice, please select your choice of topping again")
        topping_name = input("Select your choice of pizza topping or enter 'no' to finish ")
    while topping_name != 'no':
        if topping_name in pizza_topings_available_at_store:
            selected_toppings.append(topping_name)
            print(f"{topping_name} placed in your order")
        topping_name = input("Add another pizza topping to your order or type 'no' to finish ")
        while topping_name not in pizza_topings_available_at_store and topping_name != 'no':
            print("Invalid choice, please select your choice of topping again")
            topping_name = input("Select your choice of pizza topping or enter 'no' to finish ")
    

def calculate_total_amount():
    total = 0
    for pizza in selected_pizza:
        total += pizza_available_at_store[pizza]
    for toping in selected_toppings:
        total += pizza_topings_available_at_store[toping]
    print(f"Your total amount of money is {total}")

select_pizza()
select_toppings()
calculate_total_amount()