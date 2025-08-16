"""
Make a dictionary called favourite_places. Think of three names to use as keys
and store 1-3 favourite places for each person. Loop through the dictionary and
print each person's name and their favourite places.
"""

fav_places = {
    "dan": ["malvern", "zakopane", "mallorca"],
    "patrick": ["his_bedroom"],
    "nathan": ["poland", "vue_cinema"]
}

for person, places in fav_places.items():
    label = "places are" if len(places) > 1 else "place is"
    print(f"{person.title()}'s favourite {label}:")

    for place in places:
        formatted_place = place.replace("_"," ").title()
        print(f" -{formatted_place}")
    print()