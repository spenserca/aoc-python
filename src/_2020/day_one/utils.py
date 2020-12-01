def fix_expense_report(expense_report: [int]):
    while len(expense_report) > 0:
        current_expense = expense_report.pop(0)
        for next_expense in expense_report:
            if current_expense + next_expense == 2020:
                return current_expense * next_expense
