from _2020.day_ten.utils import get_product_of_one_and_three_jolt_differences, \
    get_count_of_distinct_adapter_configurations


def test_get_product_of_one_and_three_jolt_differences_returns_35_for_given_input():
    output_joltage = [
        '16',
        '10',
        '15',
        '5',
        '1',
        '11',
        '7',
        '19',
        '6',
        '12',
        '4',
    ]
    actual = get_product_of_one_and_three_jolt_differences(output_joltage)
    assert actual == 35


def test_get_product_of_one_and_three_jolt_differences_returns_220_for_given_input():
    output_joltage = [
        '28',
        '33',
        '18',
        '42',
        '31',
        '14',
        '46',
        '20',
        '48',
        '47',
        '24',
        '23',
        '49',
        '45',
        '19',
        '38',
        '39',
        '11',
        '1',
        '32',
        '25',
        '35',
        '8',
        '17',
        '7',
        '9',
        '4',
        '2',
        '34',
        '10',
        '3',
    ]
    actual = get_product_of_one_and_three_jolt_differences(output_joltage)
    assert actual == 220


def test_get_count_of_distinct_adapter_configurations_returns_8_for_given_input():
    output_joltage = [
        '16',
        '10',
        '15',
        '5',
        '1',
        '11',
        '7',
        '19',
        '6',
        '12',
        '4',
    ]
    actual = get_count_of_distinct_adapter_configurations(output_joltage)
    assert actual == 8


def test_get_count_of_distinct_adapter_configurations_returns_19208_for_given_input():
    output_joltage = [
        '28',
        '33',
        '18',
        '42',
        '31',
        '14',
        '46',
        '20',
        '48',
        '47',
        '24',
        '23',
        '49',
        '45',
        '19',
        '38',
        '39',
        '11',
        '1',
        '32',
        '25',
        '35',
        '8',
        '17',
        '7',
        '9',
        '4',
        '2',
        '34',
        '10',
        '3',
    ]
    actual = get_count_of_distinct_adapter_configurations(output_joltage)
    assert actual == 19208
