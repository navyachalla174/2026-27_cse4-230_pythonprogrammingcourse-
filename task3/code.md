# Hospital Billing and Patient Classification System

## 1. Problem Statement

The Hospital Billing and Patient Classification System is designed to calculate the total hospital bill based on consultation charges, diagnostic charges, and treatment charges.

The system collects patient details and calculates the total amount. It applies conditional concessions based on patient categories such as senior citizens and students.

It also validates billing constraints, such as charges being non-negative and concessions not exceeding the total bill. Finally, it classifies patients according to a payment policy, such as Fully Paid, Partial Payment, or Pending Payment.

## 2. Algorithm

Step 1: Start the program.

Step 2: Enter patient details such as name, age, and patient category.

Step 3: Enter consultation, diagnostic, and treatment charges.

Step 4: Validate the charges. All charges must be greater than or equal to zero.

Step 5: Calculate the total bill:

Total Bill = Consultation + Diagnostic + Treatment Charges.

Step 6: Apply conditional concessions:

- Senior citizens (age 60 or above): 10% concession.
- Students: 5% concession.
- Other patients: No concession.

Step 7: Calculate the final bill after concession.

Step 8: Enter the amount paid by the patient.

Step 9: Validate the payment amount. It must not be negative or greater than the final bill.

Step 10: Classify the patient:

- Fully Paid: Amount paid equals final bill.
- Partial Payment: Amount paid is less than final bill but greater than zero.
- Pending Payment: Amount paid is zero.

Step 11: Display the patient details, bill amount, concession, payment status, and remaining balance.

Step 12: Stop the program.

## 3. Flowchart
``` mermaid

flowchart TD
    A([Start]) --> B[/Enter patient details/]
    B --> C[/Enter consultation, diagnostic and treatment charges/]
    C --> D{Charges valid?}
    D -->|No| E[Display Invalid Charges]
    E --> Z([Stop])
    D -->|Yes| F[Calculate Total Bill]
    F --> G{Age >= 60?}
    G -->|Yes| H[Apply 10 percent concession]
    G -->|No| I{Student?}
    I -->|Yes| J[Apply 5 percent concession]
    I -->|No| K[No concession]
    H --> L[Calculate Final Bill]
    J --> L
    K --> L
    L --> M[/Enter amount paid/]
    M --> N{Payment valid?}
    N -->|No| O[Display Invalid Payment]
    O --> Z
    N -->|Yes| P{Amount paid equals bill?}
    P -->|Yes| Q[Fully Paid]
    P -->|No| R{Amount paid greater than zero?}
    R -->|Yes| S[Partial Payment]
    R -->|No| T[Pending Payment]
    Q --> U[Calculate Balance]
    S --> U
    T --> U
    U --> V[/Display Bill and Patient Classification/]
    V --> W([Stop])
```

## 5. Sample Input

```
===== HOSPITAL BILLING SYSTEM =====

Enter patient name: Ravi
Enter patient age: 65
Enter patient category (Student/Other): Other

Enter consultation charges: 500
Enter diagnostic charges: 1000
Enter treatment charges: 2500

Enter amount paid: 3000
```

## 6. Sample Output

```
===== HOSPITAL BILLING SYSTEM =====

Total Bill: 4000.0
Concession: 400.0
Final Bill: 3600.0

===== PATIENT BILL DETAILS =====

Patient Name: Ravi
Patient Age: 65
Total Bill: 4000.0
Concession: 400.0
Final Bill: 3600.0
Amount Paid: 3000.0
Remaining Balance: 600.0
Payment Status: Partial Payment

Billing Completed!
```

