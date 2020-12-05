from _2020.day_five.test_utils import get_highest_seat_id


def test_get_highest_seat_id_returns_44_for_given_input():
    boarding_passes = ['FBFBBFFRLR']
    actual = get_highest_seat_id(boarding_passes)
    assert actual == 357


def test_get_highest_seat_id_returns_567_for_given_input():
    boarding_passes = ['BFFFBBFRRR']
    actual = get_highest_seat_id(boarding_passes)
    assert actual == 567


def test_get_highest_seat_id_returns_119_for_given_input():
    boarding_passes = ['FFFBBBFRRR']
    actual = get_highest_seat_id(boarding_passes)
    assert actual == 119


def test_get_highest_seat_id_returns_820_for_given_input():
    boarding_passes = ['BBFFBBFRLL']
    actual = get_highest_seat_id(boarding_passes)
    assert actual == 820


def test_get_highest_seat_id_returns_820_for_all_given_input():
    boarding_passes = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']
    actual = get_highest_seat_id(boarding_passes)
    assert actual == 820
