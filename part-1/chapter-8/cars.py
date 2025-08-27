"""
Write a function that stores info about a car in a dictionary. The function
should always receive a manufacturer and model name. It should then accept
an arbitrary number of keyword arguments.
"""

def make_car(make, model, **kwargs):
    """Returns a dictionary with a car's make, model and any additional
    information that was given."""
    car_info = {
        "Make": make,
        "Model": model,
    }
    car_info.update(kwargs)
    return car_info