from _2020.day_fourteen.utils import get_sum_of_initialized_memory


def test_get_sum_of_initialized_memory_returns_165_for_given_input():
    initialization_program = [
        "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
        "mem[8] = 11",
        "mem[7] = 101",
        "mem[8] = 0"
    ]
    actual = get_sum_of_initialized_memory(initialization_program)
    assert actual == 165
