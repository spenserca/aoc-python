from _2020.day_one.utils import get_product_of_2_values_summing_to_2020, get_product_of_3_values_summing_to_2020
from _2020.utils.input_utils import get_input_lines


def day_one_part_one():
    input_lines = get_input_lines('day_one')
    expense_report = list(map(int, input_lines))
    return get_product_of_2_values_summing_to_2020(expense_report)


def day_one_part_two():
    input_lines = get_input_lines('day_one')
    expense_report = list(map(int, input_lines))
    return get_product_of_3_values_summing_to_2020(expense_report)
