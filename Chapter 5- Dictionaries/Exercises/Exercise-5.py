# Pets
# Creating dictionaries for different pets

pet_1 = {"animal": "Fish", "owner": "Amna"}
pet_2 = {"animal": "Lion", "owner": "Alina"}
pet_3 = {"animal": "parrot", "owner": "Abdullah"}

animals = (pet_1, pet_2, pet_3)

for pet in animals:
    print(f"Kind of animal: {pet['animal']}")
    print(f"Owner's Name: {pet['owner']}")
    print()  

