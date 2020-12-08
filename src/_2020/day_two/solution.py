from _2020.day_two.utils import get_valid_sled_rental_passwords, get_valid_toboggan_rental_passwords
from _2020.utils.input_utils import get_input_lines


def day_two_part_one():
    input_lines = get_input_lines('day_two')
    return len(get_valid_sled_rental_passwords(input_lines))


def day_two_part_two():
    input_lines = get_input_lines('day_two')
    return len(get_valid_toboggan_rental_passwords(input_lines))
