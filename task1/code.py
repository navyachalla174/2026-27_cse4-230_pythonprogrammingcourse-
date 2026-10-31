
# University Scholarship Allocation System

students = []
eligible = []
not_eligible = []

n = int(input("Enter number of students: "))

for i in range(n):

    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")

    aggregate = float(input("Enter aggregate marks: "))

    subjects = int(input("Enter number of subjects: "))

    marks = []

    for j in range(subjects):
        mark = float(input("Enter subject mark: "))
        marks.append(mark)

    attendance = float(input("Enter attendance percentage: "))

    income = float(input("Enter annual family income: "))

    student = {
        "name": name,
        "aggregate": aggregate,
        "marks": marks,
        "attendance": attendance,
        "income": income
    }

    # Check eligibility
    if (aggregate >= 75 and
        all(mark >= 40 for mark in marks) and
        attendance >= 75 and
        income <= 250000):

        eligible.append(student)

    else:
        not_eligible.append(student)


# Ranking eligible students
eligible.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"],
        s["name"].lower()
    )
)

# Display eligible students
print("\n===== SCHOLARSHIP MERIT LIST =====")

if eligible:
    for rank, s in enumerate(eligible, start=1):
        print("\nRank:", rank)
        print("Name:", s["name"])
        print("Aggregate Marks:", s["aggregate"])
        print("Attendance:", s["attendance"])
        print("Annual Income:", s["income"])
else:
    print("No eligible students found.")

# Display rejected students
print("\n===== NOT ELIGIBLE STUDENTS =====")

for s in not_eligible:
    print(s["name"])

print("\nScholarship Allocation Completed!")

