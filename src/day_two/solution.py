from day_two.utils import get_value_at_address_zero_after_processing
from utils.input_utils import get_lines_from_file


def get_initial_memory_state(noun: int, verb: int):
    day_two_input = get_lines_from_file('day_two').readline()
    initial_memory_state = list(map(int, day_two_input.split(',')))
    initial_memory_state[1] = noun
    initial_memory_state[2] = verb

    return initial_memory_state


def day_two_part_one():
    initial_memory_state = get_initial_memory_state(12, 2)

    return get_value_at_address_zero_after_processing(initial_memory_state)


def day_two_part_two():
    desired_output = 19690720

    for noun in range(100):
        for verb in range(100):
            initial_memory_state = get_initial_memory_state(noun, verb)
            actual_output = get_value_at_address_zero_after_processing(initial_memory_state)

            if actual_output == desired_output:
                return 100 * noun + verb
