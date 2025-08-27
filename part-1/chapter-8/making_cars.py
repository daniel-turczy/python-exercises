"""Works with cars.py to print out the car dictionaries that the make_car function made."""

from cars import make_car


car0 = make_car(
    "bmw", "220i",
    m_sport_trim=True,
    sports_tyres=True,
    seat_colour="cream"
)

car1 = make_car(
    "mazda", "mx-5", #(dream car btw)
    trim_level="homura",
    colour="soul_red",
    transmission="manual",
    engine_size="2.0L",
    hard_top=True
)

car2 = make_car(
    "toyota", "yaris",
    model_variant="gr_circuit",
    transmission="manual"
)

cars = [car0, car1, car2]

for car in cars:
    print(car)