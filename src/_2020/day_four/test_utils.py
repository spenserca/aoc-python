from _2020.day_four.utils import get_count_of_passports_with_valid_fields, has_valid_fields


def test_has_valid_fields_returns_1_when_passport_has_expected_and_optional_fields():
    passport = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm'
    actual = has_valid_fields(passport)
    assert actual == 1


def test_has_valid_fields_returns_0_when_passport_is_missing_hgt_field():
    passport = 'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929'
    actual = has_valid_fields(passport)
    assert actual == 0


def test_has_valid_fields_returns_1_when_passport_is_missing_optional_fields():
    passport = 'hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm'
    actual = has_valid_fields(passport)
    assert actual == 1


def test_get_count_of_passports_with_valid_fields_returns_2_for_given_input():
    input_lines = [
        'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
        'byr:1937 iyr:2017 cid:147 hgt:183cm',
        '',
        'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
        'hcl:#cfa07d byr:1929',
        '',
        'hcl:#ae17e1 iyr:2013',
        'eyr:2024',
        'ecl:brn pid:760753108 byr:1931',
        'hgt:179cm',
        '',
        'hcl:#cfa07d eyr:2025 pid:166559648',
        'iyr:2011 ecl:brn hgt:59in'
    ]
    actual = get_count_of_passports_with_valid_fields(input_lines)
    assert actual == 2
