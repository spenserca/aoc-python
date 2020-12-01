from _2020.day_one.utils import fix_expense_report
from _2020.utils.input_utils import get_lines_from_file


def day_one_part_one():
    input_lines = get_lines_from_file('day_one')
    expense_report = list(map(int, input_lines))
    return fix_expense_report(expense_report)
