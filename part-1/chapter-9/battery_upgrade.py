class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialise attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        """Print a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def set_odometer(self, new_mileage):
        """
        Update the odometer reading to the given value.
        Reject the change if the odometer was rolled back.
        """
        if new_mileage > self.odometer:
            self.odometer = new_mileage
        else:
            print("Don't roll odometers back!")

    def increment_odometer(self):
        """Increase the odometer attribute by 1."""
        self.odometer += 1

    def read_odometer(self):
        """Print the odometer reading (mileage)."""
        reading = f"{self.odometer} miles"
        print(reading)


class ElectricCar(Car):
    """
    A simple attempt to model an electric car.
    Inherits from the Car superclass.
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes from the parent class.
        Then initialize attribtes specific to an electic car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


class Battery():
    """A simple attempt to model a battery for the ElectricCar class."""

    def __init__(self, battery_size=40):
        self.size = battery_size
    
    def describe(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.size} - kWh battery.")

    def get_range(self):
        """Determine and print the car's range based on its battery size."""
        if self.size == 40:
            range = 150
        elif self.size == 65:
            range = 225
        
        print(f"This car can go around {range} miles on a full charge.")

    def upgrade(self):
        """Upgrade the battery_size attribute to 65 if it isn't already."""
        if self.size != 65:
            self.size = 65