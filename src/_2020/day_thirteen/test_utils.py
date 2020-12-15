from _2020.day_thirteen.utils import find_earliest_bus_to_take, find_earliest_timestamp_with_bus_departures_at_offset


def test_find_earliest_bus_to_take_returns_295_for_given_input():
    notes = [
        '939',
        '7,13,x,x,59,x,31,19'
    ]
    actual = find_earliest_bus_to_take(notes)
    assert actual == 295


def test_find_earliest_timestamp_with_bus_departures_at_offset_returns_1068781_for_given_input():
    notes = [
        '939',
        '7,13,x,x,59,x,31,19'
    ]
    actual = find_earliest_timestamp_with_bus_departures_at_offset(notes)
    assert actual == 1068781


def test_find_earliest_timestamp_with_bus_departures_at_offset_returns_3471_for_given_input():
    notes = [
        '939',
        '17,x,13,19'
    ]
    actual = find_earliest_timestamp_with_bus_departures_at_offset(notes)
    assert actual == 3471


def test_find_earliest_timestamp_with_bus_departures_at_offset_returns_754018_for_given_input():
    notes = [
        '939',
        '67,7,59,61'
    ]
    actual = find_earliest_timestamp_with_bus_departures_at_offset(notes)
    assert actual == 754018


def test_find_earliest_timestamp_with_bus_departures_at_offset_returns_779210_for_given_input():
    notes = [
        '939',
        '67,x,7,59,61'
    ]
    actual = find_earliest_timestamp_with_bus_departures_at_offset(notes)
    assert actual == 779210


def test_find_earliest_timestamp_with_bus_departures_at_offset_returns_1261476_for_given_input():
    notes = [
        '939',
        '67,7,x,59,61'
    ]
    actual = find_earliest_timestamp_with_bus_departures_at_offset(notes)
    assert actual == 1261476


def test_find_earliest_timestamp_with_bus_departures_at_offset_returns_1202161486_for_given_input():
    notes = [
        '939',
        '1789,37,47,1889'
    ]
    actual = find_earliest_timestamp_with_bus_departures_at_offset(notes)
    assert actual == 1202161486
