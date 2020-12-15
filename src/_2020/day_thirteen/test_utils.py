from _2020.day_thirteen.utils import find_earliest_bus_to_take


def test_find_earliest_bus_to_take_returns_295_for_given_input():
    notes = [
        '939',
        '7,13,x,x,59,x,31,19'
    ]
    actual = find_earliest_bus_to_take(notes)
    assert actual == 295
