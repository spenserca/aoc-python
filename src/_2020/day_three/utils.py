from math import prod


def count_trees_in_path_of_slope(coordinate_grid: [str], slope: [int]):
    x_coord = 0
    y_coord = 0
    tree_count = 0

    while y_coord < len(coordinate_grid) - 1:
        y_coord += slope[1]
        x_coord += slope[0]
        current_level = coordinate_grid[y_coord]
        if x_coord >= len(current_level):
            x_coord = x_coord - len(current_level)

        if current_level[x_coord] == '#':
            tree_count += 1

    return tree_count


def get_product_of_all_trees_in_path_of_slopes(coordinate_grid: [str], slopes: [[int]]):
    tree_counts = list(map(lambda s: count_trees_in_path_of_slope(coordinate_grid, s), slopes))

    return prod(tree_counts)
