from _2020.day_fifteen.utils import get_nth_number_spoken


def test_get_nth_number_spoken_returns_436_for_given_input():
    starting_numbers = "0,3,6"
    actual = get_nth_number_spoken(starting_numbers, 2020)
    assert actual == 436


def test_get_nth_number_spoken_returns_1_for_given_input():
    starting_numbers = "1,3,2"
    actual = get_nth_number_spoken(starting_numbers, 2020)
    assert actual == 1


def test_get_nth_number_spoken_returns_10_for_given_input():
    starting_numbers = "2,1,3"
    actual = get_nth_number_spoken(starting_numbers, 2020)
    assert actual == 10


def test_get_nth_number_spoken_returns_27_for_given_input():
    starting_numbers = "1,2,3"
    actual = get_nth_number_spoken(starting_numbers, 2020)
    assert actual == 27


def test_get_nth_number_spoken_returns_78_for_given_input():
    starting_numbers = "2,3,1"
    actual = get_nth_number_spoken(starting_numbers, 2020)
    assert actual == 78


def test_get_nth_number_spoken_returns_438_for_given_input():
    starting_numbers = "3,2,1"
    actual = get_nth_number_spoken(starting_numbers, 2020)
    assert actual == 438


def test_get_nth_number_spoken_returns_1836_for_given_input():
    starting_numbers = "3,1,2"
    actual = get_nth_number_spoken(starting_numbers, 2020)
    assert actual == 1836
