from _2020.day_eight.utils import get_accumulator_value_after_one_loop, get_accumulator_value_after_termination


def test_get_accumulator_value_after_one_loop_returns_5_for_given_input():
    boot_code = [
        "nop +0",
        "acc +1",
        "jmp +4",
        "acc +3",
        "jmp -3",
        "acc -99",
        "acc +1",
        "jmp -4",
        "acc +6",
    ]
    actual = get_accumulator_value_after_one_loop(boot_code)
    assert actual == 5


def test_get_accumulator_value_after_termination_returns_8_for_given_input():
    boot_code = [
        'nop +0',
        'acc +1',
        'jmp +4',
        'acc +3',
        'jmp -3',
        'acc -99',
        'acc +1',
        'jmp -4',
        'acc +6',
    ]
    actual = get_accumulator_value_after_termination(boot_code)
    assert actual == 8
