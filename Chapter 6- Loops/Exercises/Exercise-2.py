# Movie Tickets prize according to the age
while True :
    # Asking the user for their age
    age = input("Please enter your age (enter 'ok' to exit): ")

    # If the user wants to exit
    if age.lower() == 'ok':
        break

    # Converting the input to an integer
    age = int(age)

    # Telling the ticket price based on user age
    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15

    # Displaing the ticket price infront of the user
    print(f"The cost of your movie ticket is ${ticket_price}\n")

     #Add the ticket price to the total sum
    total_sum
