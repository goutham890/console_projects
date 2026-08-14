n = int(input("Enter the number of students: "))

students = []
roll = []
sub1 = []
sub2 = []
sub3 = []
totals = []

for i in range(n):
    name = input("Enter student name: ")
    students.append(name)

    r = int(input("Enter roll number: "))
    roll.append(r)

    s1 = int(input("Enter mark in Subject 1: "))
    sub1.append(s1)

    s2 = int(input("Enter mark in Subject 2: "))
    sub2.append(s2)

    s3 = int(input("Enter mark in Subject 3: "))
    sub3.append(s3)

    total = s1 + s2 + s3
    totals.append(total)

while True:

    print("\n========== COLLEGE MANAGEMENT SYSTEM ==========")
    print("1 - Student List")
    print("2 - Total Marks")
    print("3 - Average Marks")
    print("4 - Highest Scorer")
    print("5 - Lowest Scorer")
    print("6 - Pass Count")
    print("7 - Fail Count")
    print("8 - Grade for Each Student")
    print("9 - Exit")

    d = int(input("Choose an option: "))

    if d == 1:
        print("\nStudent List")
        for i in range(len(students)):
            print(students[i], roll[i])

    elif d == 2:
        print("\nTotal Marks")
        for i in range(len(students)):
            print(students[i], ":", totals[i])

    elif d == 3:
        print("\nAverage Marks")
        for i in range(len(students)):
            avg = totals[i] / 3
            print(students[i], ":", avg)

    elif d == 4:
        high = totals[0]
        position = 0

        for i in range(len(totals)):
            if totals[i] > high:
                high = totals[i]
                position = i

        print("\nHighest Scorer")
        print("Student :", students[position])
        print("Roll No :", roll[position])
        print("Total   :", high)

    elif d == 5:
        low = totals[0]
        position = 0

        for i in range(len(totals)):
            if totals[i] < low:
                low = totals[i]
                position = i

        print("\nLowest Scorer")
        print("Student :", students[position])
        print("Roll No :", roll[position])
        print("Total   :", low)

    elif d == 6:
        count = 0

        for i in range(len(students)):
            if sub1[i] >= 40 and sub2[i] >= 40 and sub3[i] >= 40:
                count += 1

        print("Pass Count :", count)

    elif d == 7:
        fail = 0

        for i in range(len(students)):
            if sub1[i] < 40 or sub2[i] < 40 or sub3[i] < 40:
                fail += 1

        print("Fail Count :", fail)

    elif d == 8:

        print("\nGrade for Each Student")

        for i in range(len(students)):

            avg = totals[i] / 3

            if avg >= 90:
                grade = "A+"
            elif avg >= 80:
                grade = "A"
            elif avg >= 70:
                grade = "B"
            elif avg >= 60:
                grade = "C"
            elif avg >= 50:
                grade = "D"
            else:
                grade = "F"

            print(students[i], "- Average:", avg, "- Grade:", grade)

    elif d == 9:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")