"""
Write a program that polls users about their dream vacation. Write a prompt
similar to 'If you could visit one place in the world, where would you go?'
Include a block of code that prints the results of the poll.
"""

responses = {}
polling_active = True

while polling_active:
    name = input("Please enter your name: ").title()
    dream_vacation = input("Where is your dream vacation? ").title()
    responses[name] = dream_vacation
    
    repeat = input("Will you let someone else to do the poll? (y or n): ")
    if repeat.lower() == "n": polling_active = False
    print()

print("---DREAM DESTINATIONS---")
for name, dream_vacation in responses.items():
    print(f"{name} would love to visit {dream_vacation}.")