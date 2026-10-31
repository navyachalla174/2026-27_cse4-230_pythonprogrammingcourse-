# Railway Fare and Reservation Calculator

## 1. Problem Statement

The Railway Fare and Reservation Calculator is designed to calculate railway ticket fares for multiple passengers based on travel distance, travel class, age-based concessions, reservation fees, and cancellation penalties.

The system collects passenger details such as name, age, distance, and travel class. It calculates the basic fare using distance slabs and applies age-based concessions for eligible passengers.

It also adds reservation fees to the ticket fare and calculates cancellation penalties when a passenger cancels a reservation. Finally, the system displays the total fare, concession, reservation fee, and refund amount.

## 2. Algorithm

Step 1: Start the program.

Step 2: Enter the number of passengers.

Step 3: Enter passenger details:

- Passenger name.
- Passenger age.
- Travel distance in kilometres.
- Travel class.

Step 4: Calculate basic fare using distance slabs:

- 0–100 km: ₹1.50 per km.
- 101–300 km: ₹1.20 per km after the first 100 km.
- Above 300 km: ₹1 per km after 300 km.

Step 5: Apply travel class multiplier:

- Sleeper: 1.0
- AC 3 Tier: 2.0
- AC 2 Tier: 3.0

Step 6: Apply age-based concessions:

- Children below 5 years: Free basic fare.
- Senior citizens aged 60 and above: 40% concession.
- Other passengers: No concession.

Step 7: Add reservation fee of ₹40.

Step 8: Calculate the final ticket fare.

Step 9: Ask whether the passenger wants to cancel the ticket.

Step 10: If cancelled, apply a 20% cancellation penalty on the final fare.

Step 11: Calculate the refund amount.

Step 12: Display passenger-wise fare details and total amount.

Step 13: Stop the program.

## 3. Flowchart
``` mermaid


flowchart TD
    A([Start]) --> B[/Enter number of passengers/]
    B --> C[/Enter passenger name, age, distance and class/]
    C --> D{Is distance valid?}
    D -->|No| E[Display Invalid Distance]
    E --> Z([Stop])
    D -->|Yes| F[Calculate Distance Slab Fare]
    F --> G[Apply Class Multiplier]
    G --> H{Age below 5?}
    H -->|Yes| I[Basic Fare = 0]
    H -->|No| J{Age >= 60?}
    J -->|Yes| K[Apply 40 percent concession]
    J -->|No| L[No Concession]
    I --> M[Add Reservation Fee]
    K --> M
    L --> M
    M --> N[Calculate Final Fare]
    N --> O{Cancel Ticket?}
    O -->|Yes| P[Calculate 20 percent Penalty]
    P --> Q[Calculate Refund]
    O -->|No| R[Ticket Confirmed]
    Q --> S[/Display Fare and Refund Details/]
    R --> S
    S --> T{More Passengers?}
    T -->|Yes| C
    T -->|No| U[Display Total Amount]
    U --> V([Stop])
```


## 5. Sample Input

```
===== RAILWAY FARE CALCULATOR =====

Enter number of passengers: 3

Passenger 1
Enter passenger name: Ravi
Enter age: 30
Enter travel distance (km): 200
Enter class (Sleeper/AC3/AC2): sleeper
Cancel ticket? (yes/no): no

Passenger 2
Enter passenger name: Sita
Enter age: 65
Enter travel distance (km): 200
Enter class (Sleeper/AC3/AC2): ac3
Cancel ticket? (yes/no): no

Passenger 3
Enter passenger name: Arun
Enter age: 25
Enter travel distance (km): 100
Enter class (Sleeper/AC3/AC2): sleeper
Cancel ticket? (yes/no): yes
```

## 6. Sample Output

```
===== RAILWAY RESERVATION STATEMENT =====

Passenger Name: Ravi
Basic Ticket Fare: 270.0
Concession: 0.0
Reservation Fee: 40
Final Fare: 310.0
Cancellation Penalty: 0
Refund Amount: 0
Ticket Status: Confirmed

Passenger Name: Sita
Basic Ticket Fare: 540.0
Concession: 360.0
Reservation Fee: 40
Final Fare: 220.0
Cancellation Penalty: 0
Refund Amount: 0
Ticket Status: Confirmed

Passenger Name: Arun
Basic Ticket Fare: 150.0
Concession: 0.0
Reservation Fee: 40
Final Fare: 190.0
Cancellation Penalty: 38.0
Refund Amount: 152.0
Ticket Status: Cancelled

Total Ticket Amount: Rs. 720.0

Railway Calculation Completed!
```

