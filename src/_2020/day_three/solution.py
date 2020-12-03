from _2020.day_three.utils import count_trees_in_path
from _2020.utils.input_utils import get_lines_from_file


def day_three_part_one():
    input_lines = list(map(lambda l: l.strip(), get_lines_from_file('day_three').readlines()))
    return count_trees_in_path(input_lines)
