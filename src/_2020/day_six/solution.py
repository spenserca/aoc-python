from _2020.day_six.utils import get_count_of_distinct_yes_answers_for_all_groups
from _2020.utils.input_utils import get_lines_from_file


def day_six_part_one():
    input_lines = get_lines_from_file('day_six')
    return get_count_of_distinct_yes_answers_for_all_groups(input_lines)
