#Seeing the word.

#  Store the locations in a list
places_to_visit = ["Murree", "Moenjodaro", "Naran Kaghan", "Swat Valley", "Neelum Valley"]

# Print your list in its original order.
print("Original order:", places_to_visit)

# Use sorted() to print your list in alphabetical order
print("Alphabetical order:", sorted(places_to_visit))

# Show that your list is still in its original order by printing it.
print("Original order:", places_to_visit)

# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print("Reverse alphabetical order:", sorted(places_to_visit, reverse=True))

# Show that your list is still in its original order by printing it again.
print("Original order:", places_to_visit)

# Use reverse() to change the order of your list. Print the list to show that its order has changed.
places_to_visit.reverse()
print("Reversed order:", places_to_visit)

#  Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
places_to_visit.reverse()
print("Original order:", places_to_visit)

# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
places_to_visit.sort()
print("Sorted in alphabetical order:", places_to_visit)

# Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
places_to_visit.sort(reverse=True)
print("Sorted in reverse alphabetical order:", places_to_visit)

