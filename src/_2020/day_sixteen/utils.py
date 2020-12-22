def parse_rules(document: [str]):
    rules = dict()
    break_index = document.index("")

    for rule in document[:break_index]:
        key, value = [r.strip() for r in rule.split(":")]

        range_values = [v.split('-') for v in value.split("or")]
        ranges = [range(int(lower_bound), int(upper_bound) + 1) for lower_bound, upper_bound in range_values]
        rules[key] = ranges

    return rules


def parse_nearby_tickets(document: [str]):
    nearby_tickets_index = document.index('nearby tickets:')

    return [[int(t) for t in nbt.split(',')] for nbt in document[nearby_tickets_index + 1:]]


def is_valid(value: int, rules: dict):
    for rule_ranges in rules.values():
        for rule_range in rule_ranges:
            if value in rule_range:
                return True

    return False


def get_scanning_error_rate(document: [str]):
    rules = parse_rules(document)
    nearby_tickets = parse_nearby_tickets(document)

    invalid_values = []
    for t in nearby_tickets:
        for value in t:
            if not is_valid(value, rules):
                invalid_values.append(value)

    return sum(invalid_values)
