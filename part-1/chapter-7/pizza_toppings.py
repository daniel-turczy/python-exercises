"""
Write a loop that prompts the user to enter a series of pizza toppings
until the enter a 'quit' value. As they enter each topping, print a message
saying you'll add that topping to their pizza.
"""

while True: 
    topping = input("What topping would you like to add? (q to quit):  ")
    if topping.lower() == "q":
        break
    else:
        message = f"Adding {topping} to your pizza.\n"
        print(message)