from _2020.day_two.utils import get_valid_passwords


def test_get_valid_passwords_returns_expected_passwords_for_given_input():
    input_lines = [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc"
    ]
    actual = get_valid_passwords(input_lines)
    assert actual == ['abcde', 'ccccccccc']
