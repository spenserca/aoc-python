from _2020.day_nine.utils import get_first_value_not_sum_of_two_preamble_values, get_sum_of_range_min_max


def test_get_first_value_not_sum_of_two_preamble_values_returns_127_for_given_input():
    port_output = [
        '35',
        '20',
        '15',
        '25',
        '47',
        '40',
        '62',
        '55',
        '65',
        '95',
        '102',
        '117',
        '150',
        '182',
        '127',
        '219',
        '299',
        '277',
        '309',
        '576',
    ]
    actual = get_first_value_not_sum_of_two_preamble_values(port_output, 5)
    assert actual == 127


def test_get_sum_of_range_min_max_returns_62_for_given_input():
    port_output = [
        '35',
        '20',
        '15',
        '25',
        '47',
        '40',
        '62',
        '55',
        '65',
        '95',
        '102',
        '117',
        '150',
        '182',
        '127',
        '219',
        '299',
        '277',
        '309',
        '576',
    ]
    actual = get_sum_of_range_min_max(port_output, 5)
    assert actual == 62
