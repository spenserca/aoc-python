from _2020.day_sixteen.utils import get_scanning_error_rate
from _2020.utils.input_utils import get_input_lines


def day_sixteen_part_one():
    input_lines = get_input_lines('day_sixteen')
    return get_scanning_error_rate(input_lines)
