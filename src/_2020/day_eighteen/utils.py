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


def get_addition_expressions(expression: str):
    return re.findall("([0-9]+\\s\\+\\s[0-9]+)", expression)


def evaluate_expression(expression: str):
    sub_expressions = get_sub_expressions(expression)

    while len(sub_expressions) > 0:
        for se in sub_expressions:
            sub_expression = se.replace('(', '').replace(')', '')
            value = evaluate(sub_expression)
            expression = expression.replace(se, str(value))

        sub_expressions = get_sub_expressions(expression)

    return evaluate(expression)


def evaluate_in_reverse_precedence(sub_expression: str):
    addition_expressions = get_addition_expressions(sub_expression)

    for ae in addition_expressions:
        value = evaluate(ae)
        sub_expression = sub_expression.replace(ae, str(value))

    return evaluate(sub_expression)


def evaluate_expression_in_reverse_precedence(expression: str):
    sub_expressions = get_addition_expressions(expression)

    while len(sub_expressions) > 0:
        for se in sub_expressions:
            sub_expression = se.replace('(', '').replace(')', '')
            value = evaluate_in_reverse_precedence(sub_expression)
            expression = expression.replace(se, str(value))

        sub_expressions = get_sub_expressions(expression)

    return evaluate_in_reverse_precedence(expression)
