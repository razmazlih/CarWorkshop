from .actions import CarManager

def print_menu():
    print("Car Management Menu")
    print("1. Add a new car")
    print("2. Get car prices")
    print("3. Delete a car")
    print("4. Search for a car")
    print("5. Exit")

def main():
    car_manager = CarManager()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter owner name: ")
            engine = input("Engine problem - 2000 NIS (yes/no): ").lower() == 'yes'
            breaks = input("Breaks problem - 1000 NIS (yes/no): ").lower() == 'yes'
            small_treatment = input("Small treatment needed - 500 NIS (yes/no): ").lower() == 'yes'
            full_treatment = input("Full treatment needed - 1000 NIS (yes/no): ").lower() == 'yes'
            filters_oil = input("Filters and oil needed - 250 NIS (yes/no): ").lower() == 'yes'
            gear = input("Gear problem - 1000 NIS (yes/no): ").lower() == 'yes'

            car_manager.add_car(name, engine, breaks, small_treatment, full_treatment, filters_oil, gear)
            print(f"\n{car_manager.search_car(name)}")
            agree = input("Do you agree? (yes/no): ").lower() == 'yes'
            if agree:
                print(f"Car {name} added successfully.")
            else:
                car_manager.delete_car(name)

        elif choice == '2':
            prices = car_manager.get_prices()
            print(prices)

        elif choice == '3':
            name = input("Enter the name of the car to delete: ")
            car_manager.delete_car(name)
            print(f"Car {name} deleted successfully.")

        elif choice == '4':
            name = input("Enter the name of the car to search for: ")
            result = car_manager.search_car(name)
            print(result)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")
