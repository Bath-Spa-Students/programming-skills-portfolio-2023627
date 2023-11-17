# Make a list of sandwich orders with 'pastrami' appearing at least three times
sandwich_orders = ["Tuna", "Cheese sandwich", "Zinger", "Vegetarian", "Pastrami", "Pastrami", "Pastrami"]

# Make an empty list for finished sandwiches
finished_sandwiches = []

# Print a message indicating the deli has run out of pastrami
print("Sorry, the deli has run out of pastrami.")

# Remove all occurrences of 'pastrami' from sandwich_orders using a while loop
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

# Loop through the remaining sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  # Take the first sandwich order

    # Check if the sandwich is not 'pastrami'
    if current_sandwich.lower() != 'pastrami':
        # Print a message for each order
        print(f"I made your {current_sandwich} sandwich.")

        # Add the made sandwich to the list of finished sandwiches
        finished_sandwiches.append(current_sandwich)

# Print a message listing each sandwich that was made
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
