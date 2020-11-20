from day_one.solution import day_one_part_one, day_one_part_two
from day_two.solution import day_two_part_one, day_two_part_two


def test_day_one_part_one_returns_correct_value():
    actual = day_one_part_one()
    assert actual == 3226488


def test_day_one_part_two_returns_correct_value():
    actual = day_one_part_two()
    assert actual == 4836845


def test_day_two_part_one_returns_correct_value():
    actual = day_two_part_one()
    assert actual == 7210630


def test_day_two_part_two_returns_correct_value():
    actual = day_two_part_two()
    assert actual == 3892
