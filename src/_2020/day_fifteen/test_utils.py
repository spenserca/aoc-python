from _2020.day_fifteen.utils import get_nth_number_spoken


def test_get_nth_number_spoken_returns_expected_values_for_given_inputs():
    starting_numbers = "0,3,6"
    actual = get_nth_number_spoken(starting_numbers, 2020)
    assert actual == 436

    actual = get_nth_number_spoken(starting_numbers, 30000000)
    assert actual == 175594


def test_get_nth_number_spoken_returns_expected_values_for_given_inputs():
    starting_numbers = "1,3,2"
    actual = get_nth_number_spoken(starting_numbers, 2020)
    assert actual == 1

    actual = get_nth_number_spoken(starting_numbers, 30000000)
    assert actual == 2578


def test_get_nth_number_spoken_returns_expected_values_for_given_inputs():
    starting_numbers = "2,1,3"
    actual = get_nth_number_spoken(starting_numbers, 2020)
    assert actual == 10

    actual = get_nth_number_spoken(starting_numbers, 30000000)
    assert actual == 3544142


def test_get_nth_number_spoken_returns_expected_values_for_given_inputs():
    starting_numbers = "1,2,3"
    actual = get_nth_number_spoken(starting_numbers, 2020)
    assert actual == 27

    actual = get_nth_number_spoken(starting_numbers, 30000000)
    assert actual == 261214


def test_get_nth_number_spoken_returns_expected_values_for_given_inputs():
    starting_numbers = "2,3,1"
    actual = get_nth_number_spoken(starting_numbers, 2020)
    assert actual == 78

    actual = get_nth_number_spoken(starting_numbers, 30000000)
    assert actual == 6895259


def test_get_nth_number_spoken_returns_expected_values_for_given_inputs():
    starting_numbers = "3,2,1"
    actual = get_nth_number_spoken(starting_numbers, 2020)
    assert actual == 438

    actual = get_nth_number_spoken(starting_numbers, 30000000)
    assert actual == 18


def test_get_nth_number_spoken_returns_expected_values_for_given_inputs():
    starting_numbers = "3,1,2"
    actual = get_nth_number_spoken(starting_numbers, 2020)
    assert actual == 1836

    actual = get_nth_number_spoken(starting_numbers, 30000000)
    assert actual == 362
