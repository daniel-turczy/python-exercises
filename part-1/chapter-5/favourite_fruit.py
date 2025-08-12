"""
Make a list of your favourite fruits, and then write a series of independant
if statements that check for certain fruits in your list.

- Make a list of your three favourite fruits and call it favourite_fruits.
- Write five if statements. Each should check whether a certain kind of fruit
  is in your list. If it is, print a statement such as "You really like bananas!
"""

favourite_fruits = [
    "blueberries","raspberries","kiwis"
]

fruits_to_check = [
    "blueberries", "raspberries", "bananas",
    "kiwis", "apples"
]

for fruit in fruits_to_check:
    if fruit in favourite_fruits:
        print(f"You like {fruit}!")