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

#  1962331 too low
def get_count_of_distinct_adapter_configurations(output_joltages: [str]):
    joltages = sorted([int(oj) for oj in output_joltages])
    current_connector_joltage_rating = 0

    adapter_configurations = dict()
    i = 0
    while i <= len(joltages):
        valid_adapters = list(filter(lambda j: j - current_connector_joltage_rating <= 3, joltages[i:i + 3]))

        if i != len(joltages):
            adapter_configurations[current_connector_joltage_rating] = valid_adapters
            current_connector_joltage_rating = valid_adapters[0]
        else:
            adapter_configurations[current_connector_joltage_rating] = [current_connector_joltage_rating + 3]

        i += 1

    return len(get_connected_adapters(adapter_configurations, 0))


def get_connected_adapters(adapter_configurations: dict, source_adapter: int):
    connected_adapters = []
    for ca in adapter_configurations[source_adapter]:
        output_str = str(source_adapter)
        if ca in adapter_configurations.keys():
            child_adapters = get_connected_adapters(adapter_configurations, ca)
            for child in child_adapters:
                connected_adapters.append(output_str + '|' + str(child))
        else:
            connected_adapters.append(output_str)

    return connected_adapters
