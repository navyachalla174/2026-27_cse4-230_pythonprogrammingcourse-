# Employee Payroll and Deduction Analysis System

## 1. Problem Statement

The Employee Payroll and Deduction Analysis System is designed to calculate the monthly salary of employees based on basic pay, allowances, overtime, and incentives.

The system calculates gross salary by adding all earnings. It then applies progressive deductions based on salary slabs, such as income tax and other deductions.

Finally, the system calculates the net salary after deductions and generates a formatted salary statement containing employee details, gross salary, deductions, and final take-home salary.

## 2. Algorithm

Step 1: Start the program.

Step 2: Enter employee details such as employee name and ID.

Step 3: Enter basic pay, allowances, overtime hours, overtime rate, and incentives.

Step 4: Calculate overtime amount.

Overtime Amount = Overtime Hours × Overtime Rate.

Step 5: Calculate gross salary.

Gross Salary = Basic Pay + Allowances + Overtime Amount + Incentives.

Step 6: Calculate progressive deductions using the following assumed salary slabs:

- Up to ₹20,000: No deduction.
- ₹20,001 to ₹40,000: 5% deduction on the amount above ₹20,000.
- ₹40,001 to ₹60,000: 10% deduction on the amount above ₹40,000, plus ₹1,000.
- Above ₹60,000: 15% deduction on the amount above ₹60,000, plus ₹3,000.

Step 7: Calculate other deductions at 2% of gross salary.

Step 8: Calculate total deductions.

Step 9: Calculate net salary.

Net Salary = Gross Salary − Total Deductions.

Step 10: Display the formatted salary statement.

Step 11: Stop the program.

## 3. Flowchart
``` mermaid


flowchart TD
    A([Start]) --> B[/Enter employee details/]
    B --> C[/Enter basic pay, allowances, overtime and incentives/]
    C --> D{Are inputs valid?}
    D -->|No| E[Display Invalid Input]
    E --> Z([Stop])
    D -->|Yes| F[Calculate Overtime Amount]
    F --> G[Calculate Gross Salary]
    G --> H{Gross Salary <= 20000?}
    H -->|Yes| I[Deduction = 0]
    H -->|No| J{Gross Salary <= 40000?}
    J -->|Yes| K[Calculate 5 percent deduction]
    J -->|No| L{Gross Salary <= 60000?}
    L -->|Yes| M[Calculate 1000 plus 10 percent]
    L -->|No| N[Calculate 3000 plus 15 percent]
    I --> O[Calculate Other Deduction]
    K --> O
    M --> O
    N --> O
    O --> P[Calculate Total Deductions]
    P --> Q[Calculate Net Salary]
    Q --> R[/Display Salary Statement/]
    R --> S([Stop])
```


## 5. Sample Input

```
===== EMPLOYEE PAYROLL SYSTEM =====

Enter Employee ID: 101
Enter Employee Name: Ravi

Enter Basic Pay: 30000
Enter Allowances: 5000
Enter Overtime Hours: 10
Enter Overtime Rate: 200
Enter Incentives: 3000
```

## 6. Sample Output

```
================================
       SALARY STATEMENT
================================

Employee ID       : 101
Employee Name     : Ravi

--------------------------------
Basic Pay         : Rs. 30000
Allowances        : Rs. 5000
Overtime Amount   : Rs. 2000
Incentives        : Rs. 3000

--------------------------------
Gross Salary      : Rs. 40000.0
Progressive Tax   : Rs. 1000.0
Other Deductions  : Rs. 800.0
Total Deductions  : Rs. 1800.0

--------------------------------
Net Salary        : Rs. 38200.0
================================

Payroll Completed!
```

