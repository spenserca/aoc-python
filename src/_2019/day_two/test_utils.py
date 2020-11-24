from _2019.day_two.utils import get_value_at_address_zero_after_processing


def test_get_position_zero_after_processing_returns_2_for_given_input():
    actual = get_value_at_address_zero_after_processing([1, 0, 0, 0, 99])
    assert actual == 2


def test_get_position_zero_after_processing_returns_30_for_given_input():
    actual = get_value_at_address_zero_after_processing([1, 1, 1, 4, 99, 5, 6, 0, 99])
    assert actual == 30


def test_get_position_zero_after_processing_returns_3500_for_given_input():
    actual = get_value_at_address_zero_after_processing([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40 , 50])
    assert actual == 3500
