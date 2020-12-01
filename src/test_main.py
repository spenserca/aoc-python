import _2018.day_one.solution
import _2019.day_one.solution
import _2019.day_two.solution
import _2020.day_one.solution


def test_2018_day_one_part_one_returns_correct_value():
    actual = _2018.day_one.solution.day_one_part_one()
    assert actual == 585


def test_2019_day_one_part_one_returns_correct_value():
    actual = _2019.day_one.solution.day_one_part_one()
    assert actual == 3226488


def test_2019_day_one_part_two_returns_correct_value():
    actual = _2019.day_one.solution.day_one_part_two()
    assert actual == 4836845


def test_2019_day_two_part_one_returns_correct_value():
    actual = _2019.day_two.solution.day_two_part_one()
    assert actual == 7210630


def test_2019_day_two_part_two_returns_correct_value():
    actual = _2019.day_two.solution.day_two_part_two()
    assert actual == 3892


def test_2020_day_one_part_one_returns_correct_value():
    actual = _2020.day_one.solution.day_one_part_one()
    assert actual == 1010884
