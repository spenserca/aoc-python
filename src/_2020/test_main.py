import _2020.day_four.solution
import _2020.day_one.solution
import _2020.day_three.solution
import _2020.day_two.solution


def test_2020_day_one_part_one_returns_correct_value():
    actual = _2020.day_one.solution.day_one_part_one()
    assert actual == 1010884


def test_2020_day_one_part_two_returns_correct_values():
    actual = _2020.day_one.solution.day_one_part_two()
    assert actual == 253928438


def test_2020_day_two_part_one_returns_correct_values():
    actual = _2020.day_two.solution.day_two_part_one()
    assert actual == 378


def test_2020_day_two_part_two_returns_correct_values():
    actual = _2020.day_two.solution.day_two_part_two()
    assert actual == 280


def test_2020_day_three_part_one_returns_correct_values():
    actual = _2020.day_three.solution.day_three_part_one()
    assert actual == 289


def test_2020_day_three_part_two_returns_correct_values():
    actual = _2020.day_three.solution.day_three_part_two()
    assert actual == 5522401584


def test_2020_day_four_part_one_returns_correct_values():
    actual = _2020.day_four.solution.day_four_part_one()
    assert actual == 182
