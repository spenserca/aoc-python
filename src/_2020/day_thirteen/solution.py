from _2020.day_thirteen.utils import find_earliest_bus_to_take
from _2020.utils.input_utils import get_input_lines


def day_thirteen_part_one():
    input_lines = get_input_lines('day_thirteen')
    return find_earliest_bus_to_take(input_lines)
