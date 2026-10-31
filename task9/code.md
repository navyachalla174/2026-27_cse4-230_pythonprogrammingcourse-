# 1. Multi-Currency Travel Budget Analysis System

## 1. Problem Statement

The Multi-Currency Travel Budget Analysis System is designed to calculate and analyze travel expenses in different currencies.

The system collects travel expense details such as expense category, amount, currency, and exchange rate. It converts foreign currency expenses into the user's home currency using the supplied exchange rates.

It also includes currency conversion fees, calculates total travel expenses, and compares planned spending against the available budget. Finally, it identifies the largest expense category and displays whether the travel budget is within or above the specified limit.

## 2. Algorithm

Step 1: Start the program.

Step 2: Enter the travel budget in the home currency (INR).

Step 3: Enter the number of expense categories.

Step 4: Enter the following details for each expense:

- Expense category.
- Expense amount.
- Currency code.
- Exchange rate.

Step 5: Convert foreign currency into INR.

Converted Amount = Expense Amount × Exchange Rate.

Step 6: Calculate conversion fees.

Conversion Fee = Converted Amount × Fee Percentage / 100.

Step 7: Calculate total expense including conversion fees.

Total Expense = Converted Amount + Conversion Fee.

Step 8: Calculate total travel expenses.

Step 9: Compare total expenses with the available budget.

- If expenses are within budget, display Budget Within Limit.
- Otherwise, display Budget Exceeded.

Step 10: Identify the largest expense category.

Step 11: Display the complete travel budget report.

Step 12: Stop the program.

## 3. Flowchart
``` mermaid

flowchart TD
    A([Start]) --> B[/Enter travel budget in INR/]
    B --> C[/Enter number of expense categories/]
    C --> D[/Enter category, amount, currency and exchange rate/]
    D --> E[Convert Amount into INR]
    E --> F[Calculate Conversion Fee]
    F --> G[Calculate Total Expense]
    G --> H[Store Category Expense]
    H --> I{More Categories?}
    I -->|Yes| D
    I -->|No| J[Calculate Total Travel Expense]
    J --> K{Expense <= Budget?}
    K -->|Yes| L[Budget Within Limit]
    K -->|No| M[Budget Exceeded]
    L --> N[Identify Largest Expense Category]
    M --> N
    N --> O[/Display Travel Budget Report/]
    O --> P([Stop])
```


## 5. Sample Input

```
===== TRAVEL BUDGET ANALYSIS =====

Enter travel budget in INR: 50000
Enter conversion fee percentage: 2
Enter number of expense categories: 3

Expense 1
Enter expense category: Hotel
Enter expense amount: 100
Enter currency code: USD
Enter exchange rate to INR: 85

Expense 2
Enter expense category: Food
Enter expense amount: 50
Enter currency code: USD
Enter exchange rate to INR: 85

Expense 3
Enter expense category: Shopping
Enter expense amount: 200
Enter currency code: AED
Enter exchange rate to INR: 23
```

## 6. Sample Output

```
===== TRAVEL EXPENSE REPORT =====

Category: Hotel
Currency: USD
Converted Amount: Rs. 8500.0
Conversion Fee: Rs. 170.0
Total Expense: Rs. 8670.0

Category: Food
Currency: USD
Converted Amount: Rs. 4250.0
Conversion Fee: Rs. 85.0
Total Expense: Rs. 4335.0

Category: Shopping
Currency: AED
Converted Amount: Rs. 4600.0
Conversion Fee: Rs. 92.0
Total Expense: Rs. 4692.0

===== BUDGET ANALYSIS =====

Travel Budget: Rs. 50000.0
Total Expenses: Rs. 17697.0

Status: Budget Within Limit
Remaining Budget: Rs. 32303.0

Largest Expense Category: Hotel
Amount: Rs. 8670.0

Travel Budget Analysis Completed!
```

