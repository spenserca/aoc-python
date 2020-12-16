from _2020.day_eleven.utils import get_count_of_occupied_seats, get_count_of_line_of_site_seating_occupied_seats
from _2020.utils.input_utils import get_input_lines


def day_eleven_part_one():
    input_lines = get_input_lines('day_eleven')
    return get_count_of_occupied_seats(input_lines)


def day_eleven_part_two():
    input_lines = get_input_lines('day_eleven')
    return get_count_of_line_of_site_seating_occupied_seats(input_lines)
