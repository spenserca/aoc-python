from _2020.day_eighteen.utils import evaluate_expression


def test_evaluate_expression_returns_71_for_given_input():
    expression = "1 + 2 * 3 + 4 * 5 + 6"
    actual = evaluate_expression(expression)
    assert actual == 71


def test_evaluate_expression_returns_51_for_given_input():
    expression = "1 + (2 * 3) + (4 * (5 + 6))"
    actual = evaluate_expression(expression)
    assert actual == 51


def test_evaluate_expression_returns_26_for_given_input():
    expression = "2 * 3 + (4 * 5)"
    actual = evaluate_expression(expression)
    assert actual == 26


def test_evaluate_expression_returns_437_for_given_input():
    expression = "5 + (8 * 3 + 9 + 3 * 4 * 3)"
    actual = evaluate_expression(expression)
    assert actual == 437


def test_evaluate_expression_returns_12240_for_given_input():
    expression = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
    actual = evaluate_expression(expression)
    assert actual == 12240


def test_evaluate_expression_returns_13632_for_given_input():
    expression = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
    actual = evaluate_expression(expression)
    assert actual == 13632
