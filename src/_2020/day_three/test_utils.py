from _2020.day_three.utils import count_trees_in_path


def test_count_trees_in_path_returns_7_for_the_given_input():
    input_lines = [
        '..##.......',
        '#...#...#..',
        '.#....#..#.',
        '..#.#...#.#',
        '.#...##..#.',
        '..#.##.....',
        '.#.#.#....#',
        '.#........#',
        '#.##...#...',
        '#...##....#',
        '.#..#...#.#',
    ]
    actual = count_trees_in_path(input_lines)
    assert actual == 7
