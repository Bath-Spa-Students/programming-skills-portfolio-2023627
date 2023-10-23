#Shrinking guest list.
guests = ("Maria", "Amna", "Omama", "Ruqaia")
print("I can invite only two people for dinner.")
invited_guests = guests[:2]
for guest in guests[2:]:
    print(f"Sorry, {guest}, I can't invite you to dinner.")
for guest in invited_guests:
    print(f"{guest}, you're still invited to dinner.")
guests = ()
print("My guest list is now empty:", guests)

