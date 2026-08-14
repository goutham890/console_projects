n = int(input("Enter the number of employees: "))

names = []
salaries = []
departments = []

for i in range(n):
    name = input("Enter employee name: ")
    names.append(name)

    salary = int(input("Enter salary: "))
    salaries.append(salary)

    department = input("Enter department: ")
    departments.append(department)

while True:
    print("\n===== Employee Management Menu =====")
    print("1 - Employee List")
    print("2 - Highest Salary")
    print("3 - Lowest Salary")
    print("4 - Average Salary")
    print("5 - Employees Earning Above Average")
    print("6 - Employees in a Department Entered by the User")
    print("7 - Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        print("\nEmployee List")
        for i in range(len(names)):
            print(names[i], salaries[i], departments[i])

    elif choice == 2:
        high = salaries[0]
        position = 0

        for i in range(len(salaries)):
            if salaries[i] > high:
                high = salaries[i]
                position = i

        print("\nHighest Salary")
        print("Employee :", names[position])
        print("Salary   :", high)
        print("Department:", departments[position])

    elif choice == 3:
        low = salaries[0]
        position = 0

        for i in range(len(salaries)):
            if salaries[i] < low:
                low = salaries[i]
                position = i

        print("\nLowest Salary")
        print("Employee :", names[position])
        print("Salary   :", low)
        print("Department:", departments[position])

    elif choice == 4:
        total = 0

        for i in range(len(salaries)):
            total += salaries[i]

        avg = total / len(salaries)

        print("\nAverage Salary:", avg)

    elif choice == 5:
        total = 0

        for i in range(len(salaries)):
            total += salaries[i]

        avg = total / len(salaries)

        print("\nEmployees Earning Above Average")

        found = False

        for i in range(len(salaries)):
            if salaries[i] > avg:
                print(names[i], salaries[i])
                found = True

        if found == False:
            print("No employee earns above the average.")

    elif choice == 6:
        dept = input("Enter department: ")

        found = False

        print("\nEmployees in", dept, "Department")

        for i in range(len(departments)):
            if departments[i] == dept:
                print(names[i], salaries[i])
                found = True

        if found == False:
            print("No employees found in this department.")

    elif choice == 7:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")