def validate_passport(passport: str):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

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
    passports.append(current_passport)

    return sum([validate_passport(p) for p in passports])


def read_passports(lines):
    passport = {}
    for entry in [entry for line in lines for entry in line.split(' ')]:
        if len(entry) == 0:
            yield passport
            passport = {}
        else:
            [field, value] = entry.split(':')
            passport[field] = value
    yield passport


def has_all_fields(passport):
    for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if field not in passport:
            return False
    return True


def solve_part_1(input_lines):
    passports = read_passports(input_lines)
    return sum(1 for p in passports if has_all_fields(p))
