import json
from problems.problems import calculate_total_price, get_all_problems

cars = []

def load_cars():
    global cars
    try:
        with open('data/cars.json', 'r') as file:
            cars = json.load(file)
    except FileNotFoundError:
        cars = []

def save_cars():
    with open('data/cars.json', 'w') as file:
        json.dump(cars, file)

def list_cars():
    return cars

def add_car(car_data):
    car = {
        'car_number': car_data['car_number'],
        'problems': car_data.getlist('problems')
    }
    car['total_price'] = calculate_total_price(car['problems'])
    cars.append(car)
    save_cars()

def delete_car(car_number):
    global cars
    cars = [car for car in cars if car['car_number'] != car_number]
    save_cars()

def search_car(car_number):
    for car in cars:
        if car['car_number'] == car_number:
            return car
    return None