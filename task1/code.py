
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")
    aggregate = float(input("Enter aggregate marks: "))

    sub1 = float(input("Enter Subject 1 marks: "))
    sub2 = float(input("Enter Subject 2 marks: "))
    sub3 = float(input("Enter Subject 3 marks: "))

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    # Eligibility checking
    if (aggregate >= 75 and
        sub1 >= 40 and
        sub2 >= 40 and
        sub3 >= 40 and
        attendance >= 75 and
        income <= 250000):

        students.append({
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })

# Ranking eligible students
students.sort(
    key=lambda x: (
        -x["aggregate"],
        -x["attendance"],
        x["income"]
    )
)

# Display results
print("\n--- SCHOLARSHIP ELIGIBILITY RESULTS ---")

if len(students) == 0:
    print("No eligible students found.")

else:
    for rank, student in enumerate(students, start=1):
        print("\nRank:", rank)
        print("Name:", student["name"])
        print("Aggregate:", student["aggregate"])
        print("Attendance:", student["attendance"])
        print("Family Income:", student["income"])

print("\nTotal Eligible Students:", len(students))

