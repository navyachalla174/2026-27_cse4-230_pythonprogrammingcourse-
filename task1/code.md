
## 1. Problem Statement

The University Scholarship Allocation System is designed to evaluate students based on their academic performance, subject-wise minimum marks, attendance percentage, and annual family income.

The system checks whether each student satisfies all the scholarship eligibility criteria. Eligible students are ranked based on their aggregate marks. If two or more students have equal aggregate marks, ties are resolved using predefined rules such as higher attendance, lower family income, and alphabetical order of names.

Finally, the system displays the list of eligible students in merit order and identifies students who are not eligible.

## 2. Algorithm

Step 1: Start the program.

Step 2: Read the number of students.

Step 3: For each student, enter:

- Student name
- Aggregate marks
- Subject-wise marks
- Attendance percentage
- Annual family income

Step 4: Check the eligibility criteria:

- Aggregate marks must be at least 75%.
- Each subject mark must be at least 40%.
- Attendance must be at least 75%.
- Annual family income must not exceed ₹2,50,000.

Step 5: If all conditions are satisfied, declare the student eligible.

Step 6: Otherwise, declare the student not eligible.

Step 7: Sort eligible students based on:

1. Higher aggregate marks.
2. Higher attendance percentage.
3. Lower annual family income.
4. Alphabetical order of student name.

Step 8: Display the ranked eligible students.

Step 9: Display the not eligible students.

Step 10: Stop the program.

## 3. Flowchart(mermaid id)
 flowchart TD
``` mermarid

flowchart TD
    A([Start]) --> B[/Enter number of students/]
    B --> C[/Enter name, aggregate marks, subject marks, attendance and income/]
    C --> D{Aggregate >= 75?}
    D -->|No| H[Not Eligible]
    D -->|Yes| E{All subject marks >= 40?}
    E -->|No| H
    E -->|Yes| F{Attendance >= 75?}
    F -->|No| H
    F -->|Yes| G{Income <= 250000?}
    G -->|No| H
    G -->|Yes| I[Declare Eligible]
    I --> J[Store Eligible Student]
    H --> K{More Students?}
    J --> K
    K -->|Yes| C
    K -->|No| L[Sort Eligible Students]
    L --> M[Apply Tie-Breaking Rules]
    M --> N[/Display Merit List and Rejected List/]
    N --> O([Stop])
    ```

## 5. Sample Input

```
Enter number of students: 3

Enter details of Student 1
Enter student name: Ravi
Enter aggregate marks: 85
Enter number of subjects: 3
Enter subject mark: 80
Enter subject mark: 90
Enter subject mark: 85
Enter attendance percentage: 90
Enter annual family income: 200000

Enter details of Student 2
Enter student name: Sita
Enter aggregate marks: 92
Enter number of subjects: 3
Enter subject mark: 95
Enter subject mark: 90
Enter subject mark: 91
Enter attendance percentage: 95
Enter annual family income: 180000

Enter details of Student 3
Enter student name: Arun
Enter aggregate marks: 70
Enter number of subjects: 3
Enter subject mark: 75
Enter subject mark: 70
Enter subject mark: 65
Enter attendance percentage: 85
Enter annual family income: 150000
```

## 6. Sample Output

```
===== SCHOLARSHIP MERIT LIST =====

Rank: 1
Name: Sita
Aggregate Marks: 92.0
Attendance: 95.0
Annual Income: 180000.0

Rank: 2
Name: Ravi
Aggregate Marks: 85.0
Attendance: 90.0
Annual Income: 200000.0

===== NOT ELIGIBLE STUDENTS =====
Arun

Scholarship Allocation Completed!
```

