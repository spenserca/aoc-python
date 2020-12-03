from _2020.day_three.utils import count_trees_in_path_of_slope, get_product_of_all_trees_in_path_of_slopes


def test_count_trees_in_path_of_slope_returns_7_for_the_given_input():
    slope = [3, 1]
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
    actual = count_trees_in_path_of_slope(input_lines, slope)
    assert actual == 7


def test_get_product_of_all_trees_in_path_of_slopes_returns_336_for_the_given_input():
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
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
    actual = get_product_of_all_trees_in_path_of_slopes(input_lines, slopes)
    assert actual == 336
