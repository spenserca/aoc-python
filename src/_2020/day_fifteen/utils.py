def get_nth_number_spoken(starting_numbers: str, n: int):
    spoken_numbers = dict()
    turn = 1
    last_number_spoken = ''

    for number in starting_numbers.split(','):
        spoken_numbers[number] = [turn]
        turn += 1
        last_number_spoken = number

    while turn <= n:
        next_number_spoken: str

        if len(spoken_numbers[last_number_spoken]) == 1:
            next_number_spoken = '0'
        else:
            turns_spoken = spoken_numbers[last_number_spoken]
            previous_two_turns_spoken = turns_spoken[len(turns_spoken) - 2:]
            next_number_spoken = str(previous_two_turns_spoken[1] - previous_two_turns_spoken[0])

        if next_number_spoken in spoken_numbers:
            spoken_numbers[next_number_spoken].append(turn)
        else:
            spoken_numbers[next_number_spoken] = [turn]

        last_number_spoken = next_number_spoken
        turn += 1

    return int(last_number_spoken)
