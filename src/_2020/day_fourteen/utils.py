import re


def parse_instructions(initialization_program: [str]):
    instructions = dict()

    current_mask: str = ''
    for instruction in initialization_program:
        if 'mask' in instruction:
            current_mask = instruction.split('=')[1].strip()
            instructions[current_mask] = []
        else:
            raw_mem_parts = [mem_parts.strip() for mem_parts in instruction.split('=')]
            address = int(re.findall('[0-9]+', raw_mem_parts[0])[0])
            value = bin(int(raw_mem_parts[1]))[2:]
            mem_parts = (address, value)
            instructions[current_mask].append(mem_parts)

    return instructions


def apply_mask(bits: str, mask: str):
    for i in range(len(mask)):
        mask_bit = mask[i]
        if mask_bit != 'X':
            bits = bits[:i] + mask_bit + bits[i + 1:]

    return bits


def get_sum_of_initialized_memory(initialization_program: [str]):
    bits = '000000000000000000000000000000000000'
    instructions = parse_instructions(initialization_program)

    for mask in instructions:
        mem_values = instructions[mask]
        for (address, value) in mem_values:
            print(str(address) + ' ' + str(value))

        bits = apply_mask(bits, mask)

    return -1
