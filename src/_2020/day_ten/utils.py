from math import prod


def get_product_of_one_and_three_jolt_differences(output_joltages: [str]):
    joltages = sorted([int(oj) for oj in output_joltages])
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


def get_count_of_distinct_adapter_configurations(output_joltages: [str]):
    return -1
