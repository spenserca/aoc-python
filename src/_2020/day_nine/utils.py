def is_sum_of_two_preamble_values(preamble: [int], number: int):
    for i in range(len(preamble)):
        first_number = preamble[i]
        other_numbers = preamble[i + 1:]
        sums = [first_number + on for on in other_numbers]
        if number in sums:
            return True

    return False


def get_first_value_not_sum_of_two_preamble_values(port_output: [str], preamble_length: int):
    port_output_ints = [int(po) for po in port_output]

    i = 0
    while i < len(port_output) - preamble_length:
        preamble = port_output_ints[i:preamble_length + i]
        number = port_output_ints[preamble_length + i]

        if not is_sum_of_two_preamble_values(preamble, number):
            return number

        i += 1

    return -1


def get_sum_of_range_min_max(port_output: [str], preamble_length: int):
    port_output_ints = [int(po) for po in port_output]
    value = get_first_value_not_sum_of_two_preamble_values(port_output_ints, preamble_length)

    for i in range(len(port_output)):
        sum_of_range = -value
        count = 1
        while sum_of_range <= value:
            num_range = port_output_ints[i:i + count]
            sum_of_range = sum(num_range)
            if sum_of_range == value:
                return min(num_range) + max(num_range)
            count += 1

    return -1
