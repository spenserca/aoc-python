from _2020.day_eleven.utils import get_count_of_occupied_seats


def test_get_count_of_occupied_seats_returns_37_for_given_input():
    seat_layout = [
        "L.LL.LL.LL",
        "LLLLLLL.LL",
        "L.L.L..L..",
        "LLLL.LL.LL",
        "L.LL.LL.LL",
        "L.LLLLL.LL",
        "..L.L.....",
        "LLLLLLLLLL",
        "L.LLLLLL.L",
        "L.LLLLL.LL",
    ]
    actual = get_count_of_occupied_seats(seat_layout)
    assert actual == 37
