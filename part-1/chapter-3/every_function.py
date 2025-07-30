"""
Think of things you could store in a list. Write a program that creates a list
containing these items and then use each function introduced in this chapter
at least once.
"""

cities = ["Worcester","Birmingham","Manchester","Liverpool","Leeds"]


print(", ".join(cities))

cities.append("Brighton")
print(f"Append Brighton: {cities}")

cities.remove("Manchester")
print(f"Remove Manchester: {cities}")

cities.insert(3,"Blackpool")
print(f"Insert Blackpool: {cities}")

popped_city = cities.pop(2)
print(f"Popped {popped_city}: {cities}")

cities.reverse()
print(f"Reversed: {cities}")

print(f"Sorted: {sorted(cities)}")
print(f"TOTAL CITIES = {len(cities)}")