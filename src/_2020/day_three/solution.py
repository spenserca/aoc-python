from _2020.day_three.utils import count_trees_in_path_of_slope, get_product_of_all_trees_in_path_of_slopes
from _2020.utils.input_utils import get_lines_from_file


def day_three_part_one():
    input_lines = get_lines_from_file('day_three')
    slope = [3, 1]
    return count_trees_in_path_of_slope(input_lines, slope)


def day_three_part_two():
    input_lines = get_lines_from_file('day_three')
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    return get_product_of_all_trees_in_path_of_slopes(input_lines, slopes)
