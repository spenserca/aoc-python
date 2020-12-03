def count_trees_in_path(coordinate_grid: [str]):
    x_coord = 0
    y_coord = 0
    tree_count = 0

    while y_coord < len(coordinate_grid) - 1:
        y_coord += 1
        x_coord += 3
        current_level = coordinate_grid[y_coord]
        if x_coord >= len(current_level):
            x_coord = x_coord - len(current_level)

        if current_level[x_coord] == '#':
            tree_count += 1

    return tree_count
