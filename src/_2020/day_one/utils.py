def get_product_of_2_values_summing_to_2020(expense_report: [int]):
    while len(expense_report) > 0:
        current_expense = expense_report.pop(0)
        for next_expense in expense_report:
            if current_expense + next_expense == 2020:
                return current_expense * next_expense


def get_product_of_3_values_summing_to_2020(expense_report: [int]):
    while len(expense_report) >= 3:
        first_expense = expense_report.pop(0)

        for i in range(len(expense_report)):
            second_expense = expense_report[i]

            if first_expense + second_expense < 2020:
                for j in range(i + 1, len(expense_report)):
                    third_expense = expense_report[j]

                    if first_expense + second_expense + third_expense == 2020:
                        return first_expense * second_expense * third_expense
