

def get_position_zero_after_processing(program: [int]):
    op_code_index = 0
    op_code = program[op_code_index]

    while op_code != 99:
        first_index_to_read = program[op_code_index + 1]
        second_index_to_read = program[op_code_index + 2]
        write_index = program[op_code_index + 3]

        if op_code == 1:
            program[write_index] = program[first_index_to_read] + program[second_index_to_read]
        elif op_code == 2:
            program[write_index] = program[first_index_to_read] * program[second_index_to_read]

        op_code_index += 4
        op_code = program[op_code_index]

    return program[0]
