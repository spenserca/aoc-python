from _2020.day_twelve.utils import get_final_location_manhattan_distance


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
