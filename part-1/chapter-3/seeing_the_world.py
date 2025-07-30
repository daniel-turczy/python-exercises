"""
Think of at least five places in the world you'd like to visit.
Store the locations in a list. Make sure the list is not in alphabetical
order.
Print the unordered list, use sorted(), use reverse sorted(), use reverse(),
use reverse() again, use sort(), use reverse() sort to put it in reverse
alphabetical order.
Print after every method to prove that it works.
"""

places_to_visit = ["Zakopane","Greece","Rome","America","Portugal"]

#sorted
print(f"Original: {places_to_visit}")
print(f"Sorted: {sorted(places_to_visit)}")
print(f"Original: {places_to_visit}")
print(f"Reverse sorted: {sorted(places_to_visit, reverse=True)}")
print(f"Original: {places_to_visit}\n")

#reverse()
places_to_visit.reverse()
print(f"Reverse: {places_to_visit}")
places_to_visit.reverse()
print(f"Reverse again: {places_to_visit}\n")

#sort()
places_to_visit.sort()
print(f"Sort: {places_to_visit}")
places_to_visit.sort(reverse=True)
print(f"Reverse sort: {places_to_visit}")