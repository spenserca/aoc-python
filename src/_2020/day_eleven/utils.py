def get_count_of_adjacent_occupied_seats(seat_position: (int, int), seat_layout: [str]):
    occupied_seat_count = 0
    x, y = seat_position
    y_range = list(filter(lambda val: 0 <= val < len(seat_layout), [y - 1, y, y + 1]))
    x_range = list(filter(lambda val: 0 <= val < len(seat_layout[y]), [x - 1, x, x + 1]))

    for _y in y_range:
        for _x in x_range:
            adjacent_seat = seat_layout[_y][_x]
            if adjacent_seat == '#':
                occupied_seat_count += 1

    if is_occupied(seat_layout[y][x]):
        return occupied_seat_count - 1
    else:
        return occupied_seat_count


def is_open(seat: str):
    return seat == 'L'


def is_occupied(seat: str):
    return seat == '#'


def update_row(row: str, index_to_update: int, updated_value: str):
    updated_row = ''

    for i in range(len(row)):
        if i == index_to_update:
            updated_row += updated_value
        else:
            updated_row += row[i]

    return updated_row


def get_count_of_occupied_seats(seat_layout: [str]):
    updated_seat_layout = [sl for sl in seat_layout]
    seat_layouts_match = False

    while not seat_layouts_match:
        previous_seat_layout = [usl for usl in updated_seat_layout]

        for y in range(len(seat_layout)):
            for x in range(len(seat_layout[y])):
                seat = previous_seat_layout[y][x]

                if seat != '.':
                    adjacent_occupied_seats = get_count_of_adjacent_occupied_seats((x, y), previous_seat_layout)
                    if is_open(seat) and adjacent_occupied_seats == 0:
                        current_row = updated_seat_layout[y]
                        updated_row = update_row(current_row, x, '#')
                        updated_seat_layout[y] = updated_row
                    elif is_occupied(seat) and adjacent_occupied_seats >= 4:
                        current_row = updated_seat_layout[y]
                        updated_row = update_row(current_row, x, 'L')
                        updated_seat_layout[y] = updated_row

        seat_layouts_match = updated_seat_layout == previous_seat_layout

    return sum([r.count('#') for r in updated_seat_layout])
