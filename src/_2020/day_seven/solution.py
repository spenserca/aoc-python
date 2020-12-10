from _2020.day_seven.utils import get_count_of_bags_containing_bag_type, get_count_of_total_bags_for_bag_type
from _2020.utils.input_utils import get_input_lines


def day_seven_part_one():
    input_lines = get_input_lines('day_seven')
    return get_count_of_bags_containing_bag_type(input_lines, 'shiny gold')


def day_seven_part_two():
    input_lines = get_input_lines('day_seven')
    return get_count_of_total_bags_for_bag_type(input_lines, 'shiny gold')
