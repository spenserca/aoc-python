from _2020.day_one.utils import get_product_of_2_values_summing_to_2020, get_product_of_3_values_summing_to_2020


def test_get_product_of_2_values_summing_to_2020_returns_514579_for_input():
    expense_report = [1721, 979, 366, 299, 675, 1456]
    actual = get_product_of_2_values_summing_to_2020(expense_report)
    assert actual == 514579


def test_get_product_of_3_values_summing_to_2020_returns_241861950_for_input():
    expense_report = [1721, 979, 366, 299, 675, 1456]
    actual = get_product_of_3_values_summing_to_2020(expense_report)
    assert actual == 241861950
