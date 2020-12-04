from _2020.day_four.utils import get_count_of_valid_passports
from _2020.utils.input_utils import get_lines_from_file


def day_four_part_one():
    input_lines = get_lines_from_file('day_four')
    return get_count_of_valid_passports(input_lines)
