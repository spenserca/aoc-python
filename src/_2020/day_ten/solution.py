from _2020.day_ten.utils import get_product_of_one_and_three_jolt_differences, \
    get_count_of_distinct_adapter_configurations
from _2020.utils.input_utils import get_input_lines


def day_ten_part_one():
    input_lines = get_input_lines('day_ten')
    return get_product_of_one_and_three_jolt_differences(input_lines)


def day_ten_part_two():
    input_lines = get_input_lines('day_ten')
    return get_count_of_distinct_adapter_configurations(input_lines)
