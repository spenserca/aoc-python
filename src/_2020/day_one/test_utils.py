from _2020.day_one.utils import fix_expense_report


def test_fix_expense_report():
    expense_report = [1721, 979, 366, 299, 675, 1456]
    actual = fix_expense_report(expense_report)
    assert actual == 514579
