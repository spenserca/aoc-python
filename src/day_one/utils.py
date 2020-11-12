from math import floor


def calculate_required_fuel_for_mass(mass: int):
    return floor(mass / 3) - 2


def calculate_total_required_fuel_for_modules(module_masses: [int]):
    return sum(map(calculate_required_fuel_for_mass, module_masses))


def calculate_required_fuel_for_module_plus_fuel(module_mass: int):
    total_required_fuel = 0
    mass = module_mass

    while calculate_required_fuel_for_mass(mass) > 0:
        fuel_required = calculate_required_fuel_for_mass(mass)
        total_required_fuel += fuel_required
        mass = fuel_required

    return total_required_fuel


def calculate_total_required_fuel_for_modules_and_fuel(module_masses: [int]):
    return sum(map(calculate_required_fuel_for_module_plus_fuel, module_masses))
