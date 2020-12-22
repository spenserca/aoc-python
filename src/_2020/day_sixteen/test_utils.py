from _2020.day_sixteen.utils import get_scanning_error_rate


def test_get_scanning_error_rate():
    document = [
        "class: 1-3 or 5-7",
        "row: 6-11 or 33-44",
        "seat: 13-40 or 45-50",
        "",
        "your ticket:",
        "7,1,14",
        "",
        "nearby tickets:",
        "7,3,47",
        "40,4,50",
        "55,2,20",
        "38,6,12"
    ]
    actual = get_scanning_error_rate(document)
    assert actual == 71
