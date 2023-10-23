#Change guest list.
guests = ["Ruqaia", "Amna", "Omama"]
busy_person = "Ruqaia"
print(f"Sadly, {busy_person} can't make it to the party.\n")
new_guest = "Maria"
guests.remove(busy_person)
guests.append(new_guest)
for guest in guests:
    invitation = f"Dear {guest},\n\nYou are invited to our guest party. We would be happy if you could join us. Please let us know if you can make it or not. Your sincerely, Sana"
    print(invitation)
