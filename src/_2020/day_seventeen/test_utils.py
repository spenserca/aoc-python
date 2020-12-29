from _2020.day_seventeen.utils import get_count_of_active_cubes


def test_get_count_of_active_cubes_returns_112_for_given_input():
    region = [
        ".#.",
        "..#",
        "###"
    ]
    actual = get_count_of_active_cubes(region)
    assert actual == 112
