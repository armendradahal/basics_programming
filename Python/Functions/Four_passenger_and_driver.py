# Problem statement :
# ==========================================================================
# A car can hold passenger and one driver, allowing five people to travel.
# Create a function that takes a number of people and print how many cars
# needed to seat everyone compfortably.
# ==========================================================================


def four_passenger_and_driver(no_of_people):
    no_of_cars = no_of_people // 5
    remaining_people = no_of_people % 5

    if remaining_people > 0:
        no_of_cars = no_of_cars + 1

    print(no_of_cars)


no_of_people = int(input())

four_passenger_and_driver(no_of_people)
