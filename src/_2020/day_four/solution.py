from _2020.day_four.utils import get_count_of_passports_with_valid_fields, \
    get_count_of_passports_with_valid_fields_and_data
from _2020.utils.input_utils import get_lines_from_file


def day_four_part_one():
    input_lines = get_lines_from_file('day_four')
    return get_count_of_passports_with_valid_fields(input_lines)


def day_four_part_two():
    input_lines = get_lines_from_file('day_four')
    return get_count_of_passports_with_valid_fields_and_data(input_lines)
