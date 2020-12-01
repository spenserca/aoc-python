def get_product_of_2_values_summing_to_2020(expense_report: [int]):
    for i in range(len(expense_report)):
        first_expense = expense_report[i]

        for j in range(i + 1, len(expense_report)):
            second_expense = expense_report[j]

            if first_expense + second_expense == 2020:
                return first_expense * second_expense


def get_product_of_3_values_summing_to_2020(expense_report: [int]):
    for i in range(len(expense_report)):
        first_expense = expense_report[i]

        for j in range(i + 1, len(expense_report)):
            second_expense = expense_report[j]

            if first_expense + second_expense < 2020:
                for k in range(j + 1, len(expense_report)):
                    third_expense = expense_report[k]

                    if first_expense + second_expense + third_expense == 2020:
                        return first_expense * second_expense * third_expense
