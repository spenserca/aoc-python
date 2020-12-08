from _2020.day_five.test_utils import get_highest_seat_id
from _2020.day_five.utils import get_missing_seat_id
from _2020.utils.input_utils import get_input_lines


def day_five_part_one():
    input_lines = get_input_lines('day_five')
    return get_highest_seat_id(input_lines)


def day_five_part_two():
    input_lines = get_input_lines('day_five')
    return get_missing_seat_id(input_lines)
