from day_two.utils import get_position_zero_after_processing
from utils.input_utils import get_lines_from_file


def day_two_part_one():
    day_two_input = get_lines_from_file('day_two').readline()
    program = list(map(int, day_two_input.split(',')))
    program[1] = 12
    program[2] = 2

    return get_position_zero_after_processing(program)


def day_two_part_two():
    return -1
