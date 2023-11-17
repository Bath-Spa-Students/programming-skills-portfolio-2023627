#Pizza toppings

pizza_toppings = []

while True:
    #  to ask the user to enter a topping
    topping = input("Enter a pizza topping (type 'Done' to finish): ")

    # If user went to finish
    if topping.lower() == 'done':
        break  

    # Adding the topping to the list
    pizza_toppings.append(topping)

    # Printing a message saying(adding topping wbe adding toppings to their pizza
    print(f"Adding {topping} to your pizza.")

#  Final list of toppings
print("Your pizza toppings:")
for topping in pizza_toppings:
    print(topping)
