def get_final_position(locations: [int], location_details: [str], lower_half_indicator: str, upper_half_indicator: str):
    for ld in location_details:
        if ld == lower_half_indicator:
            locations = locations[:int(len(locations) / 2)]
        if ld == upper_half_indicator:
            locations = locations[int(len(locations) / 2):]
    return locations[0]


def get_seat_id(boarding_pass: str):
    rows = [i for i in range(128)]
    seats = [i for i in range(8)]
    row_details = boarding_pass[:7]
    seat_details = boarding_pass[7:]
    row = get_final_position(rows, row_details, 'F', 'B')
    seat = get_final_position(seats, seat_details, 'L', 'R')
    seat_id = row * 8 + seat
    return seat_id


def get_highest_seat_id(boarding_passes: [str]):
    return max(list(map(get_seat_id, boarding_passes)))


def get_missing_seat_id(boarding_passes: [str]):
    seat_ids = sorted([get_seat_id(bp) for bp in boarding_passes])

    for i in range(len(seat_ids) - 1):
        current_seat = seat_ids[i]
        next_seat = seat_ids[i + 1]
        if next_seat != current_seat + 1:
            return current_seat + 1
