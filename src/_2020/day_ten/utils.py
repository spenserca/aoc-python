from math import prod


def get_product_of_one_and_three_jolt_differences(output_joltage: [str]):
    joltages = sorted([int(oj) for oj in output_joltage])
    current_connector_joltage_rating = 0

    joltage_distribution = [0, 1]
    for joltage in joltages:
        joltage_rating_diff = joltage - current_connector_joltage_rating
        if joltage_rating_diff <= 3:
            if joltage_rating_diff == 1:
                joltage_distribution[0] += 1
            if joltage_rating_diff == 3:
                joltage_distribution[1] += 1

            current_connector_joltage_rating = joltage

    return prod(joltage_distribution)
