# Nested Decision structure.
graduation = int(input("Enter your graduation :"))
marks = float (input("Enter your class marks :"))

if graduation > 11:
    if marks >=600:
        print("You are elegible for admission")
    else:
        print ("Sorry your graduation is less than 11")
else:
        print ("your marks is less than 600")