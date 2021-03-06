from _2020.day_twelve.utils import get_final_location_manhattan_distance, \
    get_final_location_manhattan_distance_with_waypoint
from _2020.utils.input_utils import get_input_lines


def day_twelve_part_one():
    input_lines = get_input_lines('day_twelve')
    return get_final_location_manhattan_distance(input_lines)


def day_twelve_part_two():
    input_lines = get_input_lines('day_twelve')
    return get_final_location_manhattan_distance_with_waypoint(input_lines)
