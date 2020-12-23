from _2020.day_fifteen.utils import get_nth_number_spoken
from _2020.utils.input_utils import get_input_lines


def day_fifteen_part_one():
    input_lines = get_input_lines('day_fifteen')[0]
    return get_nth_number_spoken(input_lines, 2020)


def day_fifteen_part_two():
    input_lines = get_input_lines('day_fifteen')[0]
    return get_nth_number_spoken(input_lines, 30000000)
