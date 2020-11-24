from _2018.day_one.utils import get_output_frequency


def test_get_output_frequency_returns_3_for_given_input():
    given_input = ["+1", "-2", "+3", "+1"]
    actual = get_output_frequency(given_input)
    assert actual == 3


def test_get_output_frequency_returns_3_for_other_given_input():
    given_input = ["+1", "+1", "+1"]
    actual = get_output_frequency(given_input)
    assert actual == 3


def test_get_output_frequency_returns_0_for_given_input():
    given_input = ["+1", "+1", "-2"]
    actual = get_output_frequency(given_input)
    assert actual == 0


def test_get_output_frequency_returns_minus_6_for_given_input():
    given_input = ["-1", "-2", "-3"]
    actual = get_output_frequency(given_input)
    assert actual == -6
