from _2020.day_nine.utils import get_first_value_not_sum_of_two_preamble_values, get_sum_of_range_min_max
from _2020.utils.input_utils import get_input_lines


def day_nine_part_one():
    input_lines = get_input_lines('day_nine')
    return get_first_value_not_sum_of_two_preamble_values(input_lines, 25)


def day_nine_part_two():
    input_lines = get_input_lines('day_nine')
    return get_sum_of_range_min_max(input_lines, 25)
