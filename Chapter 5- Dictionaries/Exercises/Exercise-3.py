#Glossary
glossary = {
    "Variable": "We use variables as containers to store values that can bee changed.",
    "Conditional Statement":"Conditional statements in programming are like making decision in code .it can tell if the statement is true or false..",
    "Comments": "Comments are code ignored by the computer.They are mainly for humans",
    "List": "We can use lists to store data such as list of frinds or list of shopping items.",
    "Change list item": "If we forget to add something in list.In python its easy to change list with help of codes",
}

for term, definition in glossary.items():
    print(f"{term}: {definition}")

new_terms = {
    'loop': 'A .',
    'function': 'Its a reusable code that performs a specific task.',
    'tuple': 'An immutable, ordered sequence of elements.',
    'Index' : ' We use index in coding to find a specific element from list or string .',
    'input' : 'refers to the act of entering or supplying data, information, or signals into a computer or a system.',
}   

glossary.update(new_terms)

for term, definition in glossary.items():
    print(f"{term}: {definition}")


