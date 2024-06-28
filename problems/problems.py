PROBLEM_PRICES = {
    'Engine': 2000,
    'Breaks': 1000,
    '5000 km treatment': 500,
    '10000 km treatment': 1000,
    'Filters + Oil': 250,
    'Gear': 1000
}

def calculate_total_price(problems):
    total_price = sum(PROBLEM_PRICES[problem] for problem in problems)
    return total_price

def get_all_problems():
    return PROBLEM_PRICES.keys()