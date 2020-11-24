def get_value_at_address_zero_after_processing(initial_memory_state: [int]):
    instruction_pointer = 0
    op_code = initial_memory_state[instruction_pointer]

    while op_code != 99:
        first_address_to_read = initial_memory_state[instruction_pointer + 1]
        second_address_to_read = initial_memory_state[instruction_pointer + 2]
        write_address = initial_memory_state[instruction_pointer + 3]

        if op_code == 1:
            initial_memory_state[write_address] = initial_memory_state[first_address_to_read] + initial_memory_state[second_address_to_read]
        elif op_code == 2:
            initial_memory_state[write_address] = initial_memory_state[first_address_to_read] * initial_memory_state[second_address_to_read]

        instruction_pointer += 4
        op_code = initial_memory_state[instruction_pointer]

    return initial_memory_state[0]
