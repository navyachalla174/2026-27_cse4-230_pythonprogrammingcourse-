
# Employee Payroll and Deduction Analysis

print("===== EMPLOYEE PAYROLL SYSTEM =====")

# Employee details
emp_id = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")

# Salary details
basic = float(input("Enter Basic Pay: "))
allowances = float(input("Enter Allowances: "))
hours = float(input("Enter Overtime Hours: "))
rate = float(input("Enter Overtime Rate: "))
incentives = float(input("Enter Incentives: "))

# Validate inputs
if basic < 0 or allowances < 0 or hours < 0 or rate < 0 or incentives < 0:
    print("Invalid Input! Salary values cannot be negative.")

else:

    # Calculate overtime
    overtime = hours * rate

    # Calculate gross salary
    gross = basic + allowances + overtime + incentives

    # Progressive deductions
    if gross <= 20000:
        tax = 0

    elif gross <= 40000:
        tax = (gross - 20000) * 0.05

    elif gross <= 60000:
        tax = 1000 + (gross - 40000) * 0.10

    else:
        tax = 3000 + (gross - 60000) * 0.15

    # Other deductions
    other_deduction = gross * 0.02

    # Total deductions
    total_deduction = tax + other_deduction

    # Net salary
    net_salary = gross - total_deduction

    # Display salary statement
    print("\n================================")
    print("       SALARY STATEMENT")
    print("================================")

    print("Employee ID       :", emp_id)
    print("Employee Name     :", name)

    print("--------------------------------")
    print("Basic Pay         : Rs.", basic)
    print("Allowances        : Rs.", allowances)
    print("Overtime Amount   : Rs.", overtime)
    print("Incentives        : Rs.", incentives)

    print("--------------------------------")
    print("Gross Salary      : Rs.", round(gross, 2))
    print("Progressive Tax   : Rs.", round(tax, 2))
    print("Other Deductions  : Rs.", round(other_deduction, 2))
    print("Total Deductions  : Rs.", round(total_deduction, 2))

    print("--------------------------------")
    print("Net Salary        : Rs.", round(net_salary, 2))
    print("================================")

    print("Payroll Completed!")

