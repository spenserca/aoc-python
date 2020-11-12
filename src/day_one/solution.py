from day_one.utils import calculate_total_required_fuel_for_modules, calculate_total_required_fuel_for_modules_and_fuel
from utils.input_utils import get_lines_from_file


def get_module_masses():
    input_lines = get_lines_from_file('day_one')
    return map(int, input_lines)


def day_one_part_one():
    masses = get_module_masses()
    return calculate_total_required_fuel_for_modules(masses)


def day_one_part_two():
    masses = get_module_masses()
    return calculate_total_required_fuel_for_modules_and_fuel(masses)
