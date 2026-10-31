
# Multi-Currency Travel Budget Analysis

expenses = []

print("===== TRAVEL BUDGET ANALYSIS =====")

# Enter travel budget
budget = float(input("Enter travel budget in INR: "))

fee_rate = float(input("Enter conversion fee percentage: "))

n = int(input("Enter number of expense categories: "))

total_expense = 0

for i in range(n):

    print("\nExpense", i + 1)

    category = input("Enter expense category: ")

    amount = float(input("Enter expense amount: "))

    currency = input("Enter currency code: ").upper()

    rate = float(input("Enter exchange rate to INR: "))

    # Validate inputs
    if amount < 0 or rate <= 0:
        print("Invalid expense details!")
        continue

    # Convert currency into INR
    converted_amount = amount * rate

    # Calculate conversion fee
    fee = converted_amount * fee_rate / 100

    # Calculate total expense
    final_amount = converted_amount + fee

    total_expense += final_amount

    expenses.append({
        "category": category,
        "currency": currency,
        "converted": converted_amount,
        "fee": fee,
        "total": final_amount
    })

# Display expense details
print("\n===== TRAVEL EXPENSE REPORT =====")

for e in expenses:

    print("\nCategory:", e["category"])
    print("Currency:", e["currency"])
    print("Converted Amount: Rs.", round(e["converted"], 2))
    print("Conversion Fee: Rs.", round(e["fee"], 2))
    print("Total Expense: Rs.", round(e["total"], 2))

# Calculate budget balance
remaining = budget - total_expense

print("\n===== BUDGET ANALYSIS =====")

print("Travel Budget: Rs.", round(budget, 2))
print("Total Expenses: Rs.", round(total_expense, 2))

if total_expense <= budget:
    print("Status: Budget Within Limit")
    print("Remaining Budget: Rs.", round(remaining, 2))

else:
    print("Status: Budget Exceeded")
    print("Extra Amount: Rs.", round(abs(remaining), 2))

# Find largest expense category
if expenses:

    largest = max(expenses, key=lambda e: e["total"])

    print("\nLargest Expense Category:", largest["category"])
    print("Amount: Rs.", round(largest["total"], 2))

else:
    print("\nNo valid expenses entered.")

print("\nTravel Budget Analysis Completed!")

