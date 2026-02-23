class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialise restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type.lower()
        self.number_served = 0

    def describe_restaurant(self):
        """Give the restaurant's name, cuisine type, and total customers served."""
        print(f"{self.restaurant_name} has proudly served "
        f"{self.cuisine_type} meals to {self.number_served} people.")

    def open_restaurant(self):
        """Announce that the restaurant has been opened."""
        print(f"{self.restaurant_name} is now open.")

    def set_number_served(self, num):
        """
        Set the total number of customers served.
        Reject negative numbers.
        """
        if num >= 0:
            self.number_served = num
        else:
            print("You can't serve less than 0 people.")

    def increment_number_served(self, increment):
        """
        Increment the total number of customers served.
        Reject negative numbers.
        """
        if increment >= 0:
            self.number_served += increment
        else:
            print("You can't unserve customers.")


class IceCreamStand(Restaurant):
    """
    A simple attempt to model an ice cream stand.
    Subclass to Restaurant.
    """

    def __init__(self, restaurant_name, cuisine_type="Ice cream", *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def describe_restaurant(self):
        """Give the stand's name and total customeers served."""
        print(f"{self.restaurant_name} has proudly served "
        f"{self.cuisine_type} to {self.number_served} people.")

    def show_flavors(self):
        """Print all of the flavors available."""
        print("---FLAVORS---")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")