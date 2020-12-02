def build_password_policy_details(password_and_policy: str):
    pieces = password_and_policy.split(' ')
    minimum_times = int(pieces[0].split('-')[0])
    maximum_times = int(pieces[0].split('-')[1])
    value_to_check = pieces[1].replace(':', '')
    password = pieces[2]

    return {'min_times': minimum_times, 'max_times': maximum_times, 'value': value_to_check,
            'password': password}


def validate_password(password_policy_detail: dict):
    count_of_value_in_password = password_policy_detail['password'].count(password_policy_detail['value'])

    if password_policy_detail['min_times'] <= count_of_value_in_password <= password_policy_detail['max_times']:
        return password_policy_detail['password']


def get_valid_passwords(passwords_and_policies: [str]):
    password_policy_details = [build_password_policy_details(pp) for pp in passwords_and_policies]

    return list(filter(None, [validate_password(p) for p in password_policy_details]))
