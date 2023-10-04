from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Initialize the menu, coffee maker, and money machine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# Display the available menu items
print(menu.get_items())

# Get the user's input for the coffee they want (assuming the input is in lowercase)
user_input = input("What do you want? ").lower()

# Check if the selected coffee exists in the menu
if user_input in menu.get_items():
    # Find the drink object for the selected coffee
    selected_coffee = menu.find_drink(user_input)

    # Check if there are enough resources to make the selected coffee
    if coffee_maker.is_resource_sufficient(selected_coffee):
        # Calculate the cost of the selected coffee
        cost = selected_coffee.cost

        # Process payment
        if money_machine.make_payment(cost):
            print(f"Here is your {user_input}. Enjoy!")
            # Make the selected coffee
            coffee_maker.make_coffee(selected_coffee)
        else:
            print("Insufficient funds. Payment failed.")
    else:
        print(f"Sorry, we don't have enough resources to make {user_input}.")
else:
    print("Invalid choice. Please select a coffee from the menu.")

# Display the money machine's report
print(money_machine.report())

# Display the coffee maker's report
print(coffee_maker.report())
