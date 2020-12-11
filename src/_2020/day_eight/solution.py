from _2020.day_eight.utils import get_accumulator_value_after_one_loop, get_accumulator_value_after_termination
from _2020.utils.input_utils import get_input_lines


def day_eight_part_one():
    input_lines = get_input_lines('day_eight')
    return get_accumulator_value_after_one_loop(input_lines)


def day_eight_part_two():
    input_lines = get_input_lines('day_eight')
    return get_accumulator_value_after_termination(input_lines)
