import re


def evaluate(expression: str):
    output = 0
    operation = '+'

    for value in expression.split(' '):
        if value.isnumeric() and operation == '+':
            output += int(value)
        elif value.isnumeric() and operation == '*':
            output *= int(value)
        else:
            operation = value

    return output


def get_sub_expressions(expression: str):
    return re.findall("(\\([0-9\\s+*]+\\))", expression)


def evaluate_expression(expression: str):
    sub_expressions = get_sub_expressions(expression)

    while len(sub_expressions) > 0:
        for se in sub_expressions:
            sub_expression = se.replace('(', '').replace(')', '')
            value = evaluate(sub_expression)
            expression = expression.replace(se, str(value))

        sub_expressions = get_sub_expressions(expression)

    return evaluate(expression)
