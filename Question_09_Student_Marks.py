
students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

marks = []

for i in range(students):
    print("\nEnter marks for Student", i + 1)
    row = []

    for j in range(subjects):
        mark = int(input("Enter marks for Subject " + str(j + 1) + ": "))
        row.append(mark)

    marks.append(row)

print("\n----- STUDENT MARKS ANALYSIS -----")

for i in range(students):
    total = sum(marks[i])
    average = total / subjects

    print("Student", i + 1, "Total:", total)
    print("Student", i + 1, "Average:", average)

top_total = -1
top_student = 0

for i in range(students):
    total = sum(marks[i])

    if total > top_total:
        top_total = total
        top_student = i + 1

print("\nTop Performer: Student", top_student)
print("Highest Total Marks:", top_total)

print("\nSubject-wise Averages:")

for j in range(subjects):
    total = 0

    for i in range(students):
        total = total + marks[i][j]

    average = total / students
    print("Subject", j + 1, "Average:", average)

    if average < 40:
        print("Warning: Low performance in Subject", j + 1)

print("-----------------------------------")
