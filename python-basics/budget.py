def budget(salary, alowance, investments, expenses):
    total_income = salary + allowance
    total_expenses = sum(expenses)
    remaining_budget = total_income - total_expenses
    return remaining_budget
# Example usage:
salary = 3000
allowance = 500
investments = 200
expenses = [1500, 300, 200, 100]
remaining_budget = budget(salary, allowance, investments, expenses)
print(f"The remaining budget is: ${remaining_budget:.2f}")

