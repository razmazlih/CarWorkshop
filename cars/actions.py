class Car:
    # i think it would be better to define it in the class as constants or enum. although this works nicely, its too much code and maybe a bit over-complex. but very nice job!
    def __init__(
        self, engine, breaks, small_treatment, full_treatment, filters_oil, gear
    ):
        self.problems = []

        if engine:
            self.engine = 2000
            self.problems.append("Engine")
        else:
            self.engine = 0

        if breaks:
            self.breaks = 1000
            self.problems.append("Breaks")
        else:
            self.breaks = 0

        if small_treatment:
            self.small_treatment = 500
            self.problems.append("Small Treatment")
        else:
            self.small_treatment = 0

        if full_treatment:
            self.full_treatment = 1000
            self.problems.append("Full Treatment")
        else:
            self.full_treatment = 0

        if filters_oil:
            self.filters_oil = 250
            self.problems.append("Filters and Oil")
        else:
            self.filters_oil = 0

        if gear:
            self.gear = 1000
            self.problems.append("Gear")
        else:
            self.gear = 0

    def get_car_price(self):
        return (
            self.engine
            + self.breaks
            + self.small_treatment
            + self.full_treatment
            + self.filters_oil
            + self.gear
        )

    def get_car_problems(self):
        return ", ".join(self.problems)

# this is nice work. 
class CarManager:
    def __init__(self):
        self.cars = []

    def _check_have_cars(self):
        return not self.cars

    def add_car(
        self, name, engine, breaks, small_treatment, full_treatment, filters_oil, gear
    ):
        new_car = Car(
            engine, breaks, small_treatment, full_treatment, filters_oil, gear
        )
        self.cars.append((name, new_car))

    def get_prices(self):
        if self._check_have_cars():
            return "Garage is empty"

        for one_car in self.cars:
            return one_car[0] + f" problems - ({one_car[1].get_car_problems()}), price is {one_car[1].get_car_price()} NIS"

    def delete_car(self, name):
        if self._check_have_cars():
            return "Garage is empty"

        for idx, one_car in enumerate(self.cars):
            if one_car[0] == name:
                self.cars.pop(idx)

    def search_car(self, name):
        if self._check_have_cars():
            return "Garage is empty"

        for idx, one_car in enumerate(self.cars):
            if one_car[0] == name:
                return f"{name}'s car price is {one_car[1].get_car_price()} NIS"

    def get_total_profit(self):
        if self._check_have_cars():
            return ""

        total_profit = 0
        for one_car in self.cars:
            car_class = one_car[1]
            total_profit += car_class.get_car_price()

        return f"total profit is {total_profit} NIS"

all_cars = CarManager()

# all_cars.add_car("Raz", True, True, True, True, True, True)
# all_cars.add_car("Ron", True, True, True, True, True, True)

print(all_cars.get_total_profit())
