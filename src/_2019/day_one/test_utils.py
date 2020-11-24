from day_one.utils import calculate_required_fuel_for_mass, calculate_total_required_fuel_for_modules, \
    calculate_required_fuel_for_module_plus_fuel, calculate_total_required_fuel_for_modules_and_fuel


def test_calculate_required_fuel_requires_2_fuel_units_for_mass_of_12():
    actual = calculate_required_fuel_for_mass(12)
    assert actual == 2


def test_calculate_required_fuel_requires_2_fuel_units_for_mass_of_14():
    actual = calculate_required_fuel_for_mass(14)
    assert actual == 2


def test_calculate_required_fuel_requires_654_fuel_units_for_mass_of_1969():
    actual = calculate_required_fuel_for_mass(1969)
    assert actual == 654


def test_calculate_required_fuel_requires_33583_fuel_units_for_mass_of_100756():
    actual = calculate_required_fuel_for_mass(100756)
    assert actual == 33583


def test_calculate_total_required_fuel_for_modules_requires_34241_fuel_units_for_all_modules():
    actual = calculate_total_required_fuel_for_modules([12, 14, 1969, 100756])
    assert actual == 34241


def test_calculate_required_fuel_for_module_plus_fuel_requires_2_fuel_units_for_mass_of_12():
    actual = calculate_required_fuel_for_module_plus_fuel(12)
    assert actual == 2


def test_calculate_required_fuel_for_module_plus_fuel_requires_2_fuel_units_for_mass_of_14():
    actual = calculate_required_fuel_for_module_plus_fuel(14)
    assert actual == 2


def test_calculate_required_fuel_for_module_plus_fuel_requires_966_fuel_units_for_mass_of_1969():
    actual = calculate_required_fuel_for_module_plus_fuel(1969)
    assert actual == 966


def test_calculate_required_fuel_for_module_plus_fuel_requires_50346_fuel_units_for_mass_of_100756():
    actual = calculate_required_fuel_for_module_plus_fuel(100756)
    assert actual == 50346


def test_calculate_total_required_fuel_for_modules_and_fuel_requires_xxx_fuel_for_all_modules():
    actual = calculate_total_required_fuel_for_modules_and_fuel([12, 14, 1969, 100756])
    assert actual == 51316
