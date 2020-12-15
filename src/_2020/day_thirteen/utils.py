def get_next_departure_after_estimate(bus_id: int, departure_estimate: int):
    next_departure = 0
    while next_departure < departure_estimate:
        next_departure += bus_id

    return next_departure - departure_estimate


def find_earliest_bus_to_take(notes: [str]):
    departure_estimate = int(notes[0])

    bus_wait_times = dict()
    for b in notes[1].split(','):
        if b.lower() != 'x':
            wait_time = get_next_departure_after_estimate(int(b), departure_estimate)
            bus_wait_times[wait_time] = int(b)

    minimum_wait_time = min(bus_wait_times.keys())
    return minimum_wait_time * bus_wait_times[minimum_wait_time]
