"""
Start with the program you wrote for Exercise 6-1 (use a dictionary to store
info about someone you know). Make two new dictionaries and store all three
in a list called people. As you loop through the list, print everthing you
know about each person.
"""

person0 = {
    "first_name": "Chris",
    "last_name": "Davidson",
    "age": "20",
    "city": "Birmingham"
}

person1 = {
    "first_name": "Daniel",
    "last_name": "Tillota",
    "age": "16",
    "city": "Cornwall"
}

person2 = {
    "first_name": "Nathan",
    "last_name": "Karwowski",
    "age": "43",
    "city": "Birmingham"
}
people = [person0, person1, person2]

#max_key_length used to align the keys when outputted
max_key_length = max(len(k) for person in people for k in person)

for person in people:
    for category, info in person.items():
        formatted_category = category.replace("_", " ").title()
        print(f"{formatted_category:{max_key_length}} : {info.title()}")
    print()