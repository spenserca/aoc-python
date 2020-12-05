import re


def build_passports(passport_data):
    passports = []
    current_passport = {}
    for pd in passport_data:
        if pd == '':
            passports.append(current_passport)
            current_passport = {}
        else:
            attributes = pd.split(' ')
            for kv in attributes:
                [key, value] = kv.split(':')
                current_passport[key] = value
    passports.append(current_passport)
    return passports


def has_valid_fields(passport: dict):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for rf in required_fields:
        if rf not in passport:
            return False
    return True


def validate_height(height: str):
    if height.endswith('cm'):
        height_value = int(height.replace('cm', ''))
        return 150 <= height_value <= 193
    if height.endswith('in'):
        height_value = int(height.replace('in', ''))
        return 59 <= height_value <= 76
    return False


def has_valid_data(passport: dict):
    if not has_valid_fields(passport):
        return False

    has_valid_birth_year = 1920 <= int(passport['byr']) <= 2002
    has_valid_issue_year = 2010 <= int(passport['iyr']) <= 2020
    has_valid_expiration_year = 2020 <= int(passport['eyr']) <= 2030
    has_valid_height = validate_height(passport['hgt'])
    has_valid_hair_color = re.match('^#[0-9a-f]{6}$', passport['hcl'])
    has_valid_eye_color = passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    has_valid_passport_id = re.match('^[0-9]{9}$', passport['pid'])

    return has_valid_birth_year and has_valid_issue_year and has_valid_expiration_year and has_valid_height and \
           has_valid_hair_color and has_valid_eye_color and has_valid_passport_id


def get_count_of_passports_with_valid_fields(passport_data: [str]):
    return len(list(filter(has_valid_fields, build_passports(passport_data))))


def get_count_of_passports_with_valid_fields_and_data(passport_data: [str]):
    return len(list(filter(has_valid_data, build_passports(passport_data))))
