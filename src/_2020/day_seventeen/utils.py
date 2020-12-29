def build_expanded_region(region: [str]):
    expanded_region = []
    inactive_row = ''.join(['#' for i in range(len(region[0]))])
    expanded_region.append(inactive_row)
    for row in region:
        expanded_region.append('#' + row + '#')
    expanded_region.append(inactive_row)
    return expanded_region


def get_count_of_active_cubes(region: [str]):


    return build_expanded_region(region)
