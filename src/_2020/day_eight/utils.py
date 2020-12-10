def get_accumulator_value_after_one_loop(boot_code: [str]):
    accumulator = 0
    current_instruction = 0
    visited_instructions = []

    while current_instruction not in visited_instructions:
        instruction = boot_code[current_instruction]
        visited_instructions.append(current_instruction)
        op, str_arg = instruction.split(' ')
        arg = int(str_arg)

        if op == 'acc':
            accumulator += arg
            current_instruction += 1
        elif op == 'jmp':
            if arg > 0:
                # ci = 5 arg = 7 len = 10
                # move forward 12 - 10 = 2
                # end instruction should be 1 (second instruction in list)
                if current_instruction + arg > len(boot_code):
                    current_instruction = ((current_instruction + arg) - len(boot_code)) - 1
                else:
                    current_instruction += arg
            if arg < 0:
                # ci = 5, arg = -7, len = 10
                # move back 5 to 0, then wrap around to index 8 (second to last instruction)
                if current_instruction + arg < 0:
                    current_instruction = len(boot_code) - abs(current_instruction + arg)
                else:
                    current_instruction += arg
        elif op == 'nop':
            current_instruction += 1

    return accumulator
