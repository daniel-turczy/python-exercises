"""
Make a dictionary called cities. Use the names of three cities as keys and
dictionaries of information as values. Include the country, population, and a
fact in the information dictionaries. Print the name of each city and its
information.
"""

cities = {
    "birmingham": {
        "country": "england",
        "population": 2_700_000,
        "fact": "ozzy osbourne was born there."
    },

    "new_york": {
        "country": "USA",
        "population": 8_000_000,
        "fact": "it is america's biggest city."
    },

    "zakopane": {
        "country": "poland",
        "population": 30_000,
        "fact": "when on its mountains, you can cross between Slovakia and Poland."
    }
}

for name, city_info in cities.items():
    formatted_name = name.replace("_", " ").upper()
    print(formatted_name)

    for category, info in city_info.items():
        print(f"{category.title()}: {str(info).capitalize()}")
    print()