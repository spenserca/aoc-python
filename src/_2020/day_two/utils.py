def build_sled_rental_password_policy_details(password_and_policy: str):
    pieces = password_and_policy.split(' ')
    minimum_times = int(pieces[0].split('-')[0])
    maximum_times = int(pieces[0].split('-')[1])
    value_to_check = pieces[1].replace(':', '')
    password = pieces[2]

    return {'min_times': minimum_times, 'max_times': maximum_times, 'value': value_to_check,
            'password': password}


def validate_sled_rental_password(password_policy_detail: dict):
    count_of_value_in_password = password_policy_detail['password'].count(password_policy_detail['value'])

    if password_policy_detail['min_times'] <= count_of_value_in_password <= password_policy_detail['max_times']:
        return password_policy_detail['password']


def get_valid_sled_rental_passwords(passwords_and_policies: [str]):
    password_policy_details = [build_sled_rental_password_policy_details(pp) for pp in passwords_and_policies]

    return list(filter(None, [validate_sled_rental_password(p) for p in password_policy_details]))


def build_toboggan_rental_password_policy_details(password_and_policy: str):
    pieces = password_and_policy.split(' ')
    zero_based_location_one = int(pieces[0].split('-')[0]) - 1
    zero_based_location_two = int(pieces[0].split('-')[1]) - 1
    value_to_check = pieces[1].replace(':', '')
    password = pieces[2]

    return {'location_one': zero_based_location_one, 'location_two': zero_based_location_two, 'value': value_to_check,
            'password': password}


def validate_toboggan_rental_password(password_policy_detail: dict):
    value_at_location_one = password_policy_detail['password'][password_policy_detail['location_one']]
    value_at_location_two = password_policy_detail['password'][password_policy_detail['location_two']]

    if value_at_location_one == password_policy_detail['value'] and \
            value_at_location_two != password_policy_detail['value']:
        return password_policy_detail['password']
    if value_at_location_two == password_policy_detail['value'] and \
            value_at_location_one != password_policy_detail['value']:
        return password_policy_detail['password']


def get_valid_toboggan_rental_passwords(passwords_and_policies: [str]):
    password_policy_details = [build_toboggan_rental_password_policy_details(pp) for pp in passwords_and_policies]

    return list(filter(None, [validate_toboggan_rental_password(p) for p in password_policy_details]))
