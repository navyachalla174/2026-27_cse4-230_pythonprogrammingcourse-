# Progressive Electricity Billing System

## 1. Problem Statement

The Progressive Electricity Billing System is designed to calculate household electricity bills based on monthly electricity consumption.

The system calculates charges using multiple consumption slabs, fixed charges, surcharges, and rebates. It accepts electricity consumption details for several months and calculates the total bill for each month.

The system also compares monthly electricity bills and identifies unusual increases in the bill amount. Finally, it displays the monthly billing details and highlights months with significant increases.

## 2. Algorithm

Step 1: Start the program.

Step 2: Enter the number of months.

Step 3: Enter the electricity units consumed for each month.

Step 4: Calculate electricity charges using progressive slabs:

- 0–100 units: ₹2 per unit.
- 101–200 units: ₹3 per unit.
- 201–300 units: ₹5 per unit.
- Above 300 units: ₹7 per unit.

Step 5: Add fixed charges of ₹50.

Step 6: Calculate a surcharge of 5% on energy charges.

Step 7: Apply a rebate of 2% if consumption is below 100 units.

Step 8: Calculate the final bill amount.

Step 9: Compare the current month's bill with the previous month's bill.

Step 10: If the bill increases by more than 30%, identify it as an unusual increase.

Step 11: Display monthly bills and unusual increases.

Step 12: Stop the program.

## 3. Flowchart
``` mermaid

flowchart TD
    A([Start]) --> B[/Enter number of months/]
    B --> C[/Enter electricity units/]
    C --> D[Calculate slab charges]
    D --> E[Add fixed charges]
    E --> F[Calculate 5 percent surcharge]
    F --> G{Units below 100?}
    G -->|Yes| H[Apply 2 percent rebate]
    G -->|No| I[No rebate]
    H --> J[Calculate final bill]
    I --> J
    J --> K{More months?}
    K -->|Yes| C
    K -->|No| L[Compare monthly bills]
    L --> M{Bill increase above 30 percent?}
    M -->|Yes| N[Identify unusual increase]
    M -->|No| O[Normal increase]
    N --> P[Display monthly bills and results]
    O --> P
    P --> Q([Stop])
```




## 5. Sample Input

```
Enter number of months: 3

Month 1
Enter electricity units: 80

Month 2
Enter electricity units: 150

Month 3
Enter electricity units: 250
```

## 6. Sample Output

```
===== ELECTRICITY BILL DETAILS =====

Month 1
Units Consumed: 80.0
Total Bill: Rs. 211.2

Month 2
Units Consumed: 150.0
Total Bill: Rs. 367.5

Month 3
Units Consumed: 250.0
Total Bill: Rs. 682.5

===== MONTHLY BILL COMPARISON =====

Month 2
Unusual Increase Detected!
Increase Percentage: 73.86 %

Month 3
Unusual Increase Detected!
Increase Percentage: 85.71 %

Billing Calculation Completed!
```

