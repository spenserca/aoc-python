def get_new_heading(heading: str, action: str, value: int):
    heading_rotations = int(value / 90)

    for i in range(heading_rotations):
        if action == 'L':
            if heading == 'N':
                heading = 'W'
            elif heading == 'E':
                heading = 'N'
            elif heading == 'S':
                heading = 'E'
            else:
                heading = 'S'
        if action == 'R':
            if heading == 'N':
                heading = 'E'
            elif heading == 'E':
                heading = 'S'
            elif heading == 'S':
                heading = 'W'
            else:
                heading = 'N'

    return heading


def get_manhattan_distance(location):
    origin = [0, 0]

    return abs(location[0] - origin[0]) + abs(location[1] - origin[1])


def get_final_location_manhattan_distance(navigation_instructions: [str]):
    heading = 'E'
    location = [0, 0]

    for action, value in [(ni[:1], int(ni[1:])) for ni in navigation_instructions]:
        if action == 'N':
            # Action N means to move north by the given value.
            location[1] += value
        elif action == 'S':
            # Action S means to move south by the given value.
            location[1] -= value
        elif action == 'E':
            # Action E means to move east by the given value.
            location[0] += value
        elif action == 'W':
            # Action W means to move west by the given value.
            location[0] -= value
        elif action == 'L':
            # Action L means to turn left the given number of degrees.
            heading = get_new_heading(heading, action, value)
        elif action == 'R':
            # Action R means to turn right the given number of degrees.
            heading = get_new_heading(heading, action, value)
        elif action == 'F':
            # Action F means to move forward by the given value in the direction the ship is currently facing.
            if heading == 'N':
                location[1] += value
            elif heading == 'E':
                location[0] += value
            elif heading == 'S':
                location[1] -= value
            else:
                location[0] -= value

    return get_manhattan_distance(location)
