from _2020.day_eighteen.utils import evaluate_expression, evaluate_expression_in_reverse_precedence
from _2020.utils.input_utils import get_input_lines


def day_eighteen_part_one():
    input_lines = get_input_lines('day_eighteen')
    return sum([evaluate_expression(il) for il in input_lines])


def day_eighteen_part_two():
    input_lines = get_input_lines('day_eighteen')
    return sum([evaluate_expression_in_reverse_precedence(il) for il in input_lines])
