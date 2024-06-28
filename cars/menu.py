from flask import Blueprint, render_template, request, redirect, url_for
from cars.actions import list_cars, add_car, delete_car, search_car
from problems.problems import get_all_problems

car_blueprint = Blueprint('cars', __name__)

@car_blueprint.route('/')
def car_menu():
    return render_template('index.html')

@car_blueprint.route('/list')
def car_list():
    cars = list_cars()
    return render_template('view_cars.html', cars=cars)

@car_blueprint.route('/add', methods=['GET', 'POST'])
def car_add():
    if request.method == 'POST':
        car_data = request.form
        add_car(car_data)
        return redirect(url_for('cars.car_list'))
    problems = get_all_problems()
    return render_template('add_car.html', problems=problems)

@car_blueprint.route('/delete', methods=['POST'])
def car_delete():
    car_data = request.form
    delete_car(car_data['car_number'])
    return redirect(url_for('cars.car_list'))

@car_blueprint.route('/search', methods=['GET', 'POST'])
def car_search():
    if request.method == 'POST':
        car_number = request.form['car_number']
        car = search_car(car_number)
        return render_template('view_cars.html', cars=[car])
    return render_template('search_car.html')