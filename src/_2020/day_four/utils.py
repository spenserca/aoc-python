def validate_passport(passport: str):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    optional_fields = ['cid']

    for rf in required_fields:
        if passport.find(rf) == -1:
            return 0

    return 1


def get_count_of_valid_passports(passport_data: [str]):
    passports = []
    current_passport = ''

    for pd in passport_data:
        if pd == '':
            passports.append(current_passport)
            current_passport = ''
        else:
            current_passport += ' ' + pd

    return sum([validate_passport(p) for p in passports])  # 181 is too low
