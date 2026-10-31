# University Scholarship Allocation

## 1. Problem Statement

To develop a Python program that evaluates students for scholarships based on aggregate marks, subject-wise minimum marks, attendance percentage, and family income. The program identifies eligible students, ranks them according to their marks, and resolves ties using predefined rules.

## 2. Algorithm

1. Start the program.
2. Enter the number of students.
3. Enter each student's name.
4. Enter aggregate marks.
5. Enter subject-wise marks.
6. Enter attendance percentage.
7. Enter annual family income.
8. Check eligibility using the following conditions:
   - Aggregate marks must be at least 75%.
   - Each subject mark must be at least 40%.
   - Attendance must be at least 75%.
   - Annual family income must not exceed ₹2,50,000.
9. Select students who satisfy all conditions.
10. Rank eligible students based on aggregate marks in descending order.
11. If aggregate marks are equal, give priority to higher attendance.
12. If aggregate marks and attendance are equal, give priority to lower family income.
13. Display the eligible students in rank order.
14. Stop the program.

## 3. Flowchart
``` mermaid


flowchart TD
    A([Start]) --> B[/Enter student details/]
    B --> C[Check aggregate marks]
    C --> D[Check subject-wise minimum marks]
    D --> E[Check attendance]
    E --> F[Check family income]
    F --> G{All conditions satisfied?}
    G -- No --> H[Mark as Not Eligible]
    G -- Yes --> I[Add student to eligible list]
    H --> J{More students?}
    I --> J
    J -- Yes --> B
    J -- No --> K[Rank eligible students]
    K --> L[Resolve ties using attendance and income]
    L --> M[/Display scholarship ranking/]
    M --> N([Stop])
```

## 5. Sample Input

```
Enter number of students: 3

Enter details of Student 1
Enter student name: Ravi
Enter aggregate marks: 85
Enter Subject 1 marks: 80
Enter Subject 2 marks: 90
Enter Subject 3 marks: 85
Enter attendance percentage: 90
Enter annual family income: 200000

Enter details of Student 2
Enter student name: Sita
Enter aggregate marks: 90
Enter Subject 1 marks: 88
Enter Subject 2 marks: 92
Enter Subject 3 marks: 90
Enter attendance percentage: 95
Enter annual family income: 180000

Enter details of Student 3
Enter student name: Rani
Enter aggregate marks: 85
Enter Subject 1 marks: 80
Enter Subject 2 marks: 85
Enter Subject 3 marks: 90
Enter attendance percentage: 95
Enter annual family income: 150000
```

## 6. Sample Output

```
--- SCHOLARSHIP ELIGIBILITY RESULTS ---

Rank: 1
Name: Sita
Aggregate: 90.0
Attendance: 95.0
Family Income: 180000.0

Rank: 2
Name: Rani
Aggregate: 85.0
Attendance: 95.0
Family Income: 150000.0

Rank: 3
Name: Ravi
Aggregate: 85.0
Attendance: 90.0
Family Income: 200000.0

Total Eligible Students: 3
```

