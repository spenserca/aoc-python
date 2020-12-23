from _2020.day_eighteen.utils import evaluate_expression
from _2020.utils.input_utils import get_input_lines


def day_eighteen_part_one():
    input_lines = get_input_lines('day_eighteen')
    return sum([evaluate_expression(il) for il in input_lines])
