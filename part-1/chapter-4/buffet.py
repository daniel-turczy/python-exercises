"""
A buffet-style restaurant offers only five basic foods. Think of five simple
foods, and then store them in a tuple.

- Use a for loop to print each food the restaurant offers.
- Try to modify one of the items, and make sure Python rejects the change.
- The restaurant changes its menu, replacing two of the items with different
  foods. Add a line to rewrite the tuple and use a for loop to print each of the
  items on the revised menu.
"""

foods = ("pizza",
         "donner kebab",
         "hot dogs",
         "ice cream",
         "plums")

print("Original Menu:")
for food in foods:
    print("-",food)


foods = ("pizza",
         "donner kebab",
         "hot dogs",
         "chocolate bar",
         "strawberries")

print("\nRevised Menu:")
for food in foods:
    print("-",food)