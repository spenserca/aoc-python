from _2020.day_two.utils import get_valid_passwords
from _2020.utils.input_utils import get_lines_from_file


def day_two_part_one():
    input_lines = get_lines_from_file('day_two')
    return len(get_valid_passwords(input_lines))
