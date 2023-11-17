
# Making a list of sandwiches
sandwich_orders = ['Tuna', 'Cheese', 'Zinger', 'Vegetarian']

# Make an empty list for finished sandwiches
finished_sandwiches = []

# Loop through the sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  # Take the first sandwich order

    # Print a message for each order
    print(f"Your order {current_sandwich} sandwich is ready.")

    # Add the made sandwich to the list of finished sandwiches
    finished_sandwiches.append(current_sandwich)
    
    print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
