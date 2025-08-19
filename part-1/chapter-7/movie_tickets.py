"""
A movie theatre charges different ticket prices depending on a person's age.
Under 3 years old: free
3-12 years old: $10
12+ years old: $15
Write a loop in which you ask users their age, and then tell them the cost of
their movie ticket.
"""

while True:
    age = int(input("Please enter your age: ")) 
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15
    
    print(f"As you are {age}, your price is ${price}.")