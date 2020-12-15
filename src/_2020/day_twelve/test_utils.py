from _2020.day_twelve.utils import get_final_location_manhattan_distance, \
    get_final_location_manhattan_distance_with_waypoint


def test_get_final_location_manhattan_distance_return_25_for_given_input():
    navigation_instructions = [
        'F10',
        'N3',
        'F7',
        'R90',
        'F11'
    ]
    actual = get_final_location_manhattan_distance(navigation_instructions)
    assert actual == 25


def test_get_final_location_manhattan_distance_with_waypoint_returns_286_for_given_input():
    navigation_instructions = [
        'F10',
        'N3',
        'F7',
        'R90',
        'F11'
    ]
    actual = get_final_location_manhattan_distance_with_waypoint(navigation_instructions)
    assert actual == 286
