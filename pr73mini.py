#Q15 ⭐ — Mini Project: Student Management System
#Build a complete student management program.
#Each student should have:
#Name
#Age
#Course
#Marks
#The program should allow the user to:
#1. Add Student
#2. View Students
#3. Search Student
#4. Update Student
#5. Remove Student
#6. Show Topper
#7. Show Statistics
#8. Exit
#Under Statistics, display useful information such as:
#Average marks
#Highest marks
#Lowest marks
#Pass/fail count
#Above-average students

x = {}
num = int(input("enter the number of students :"))
for i in range(num):
    n = input("enter the name of student : ")
    a = int(input("enter the age of student :"))
    c = input("enter the course of student :")
    m = int(input("enter the mark of student :"))
    print("-------------------------------------------")
    x[n] = { 
        'age':a,'course':c,'mark':m
    }
while(True):
    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Remove Student")
    print("6. Show Topper")
    print("7. Show Statistics")
    print("8. Exit")
    print("==============================================")

    o = int(input("choose an option :"))

    if o == 1:
        n1 = input("enter the student name :")
        a1 = int(input("enter the age of student :"))
        c1 = input("enter the course of student :")
        m1 = int(input("enter the mark of student :"))
        x[n1] = {
            'age':a1,'course':c1,'mark':m1
        }
    if o == 2:
        for i in x:
            print(f"name : {i}")
            print(f"age : {x[i]['age']}")
            print(f"course : {x[i]['course']}")
            print(f"mark : {x[i]['mark']}")
            print("-" * 32)

    if o == 3:
        s = input("enter the name of student :")
        found = False
        for i in x:
            if i == s:
                print("student found")
                print(f"name : {i}")
                print(f"age : {x[i]['age']}")
                print(f"course : {x[i]['course']}")
                print(f"mark : {x[i]['mark']}")
                found = True
                break
        if found == False:
                print("student not found")

    if o == 4:
        u = input("enter the name of student to update :")
        while(True):
            print("1 - Age")
            print("2 - Mark")
            print("3 - Course")
            print("4 - Exit")
            ch = int(input("choose a number :"))
            if ch == 1:
                a2 = int(input("enter new age :"))
                if u in x:
                    x[u]['age'] = a2
            elif ch == 2:
                m2 = int(input("enter new mark :"))
                if u in x:
                    x[u]['mark'] = m2
            elif ch == 3:
                c2 = input("enter new course :")
                if u in x:
                    x[u]['course'] = c2
            elif ch == 4:
                break

    if o == 5:
        rem = input("enter the name of the student :")
        if rem in x:
            x.pop(rem)
        else :
            print("student not fount :")

    if o == 6:
        y = 0
        for i in x:
            if x[i]['mark'] > y:
                y = x[i]['mark']
        for i in x:
            if x[i]['mark'] == y:
                print("topper :", i)
                print("mark :", y)

    if o == 7:
        ts = 0
        high = 0
        low  = 100
        total = 0
        pas = 0
        fail = 0
        for i in x:
            ts = ts + 1
            if x[i]['mark'] > high:
                high = x[i]['mark']
            if x[i]['mark'] < low:
                low = x[i]['mark']
            total = total + x[i]['mark']
            if x[i]['mark']>= 40:
                pas = pas + 1
            else:
                fail = fail + 1
        avg = total/len(x)
        print("total student :",ts)
        print("highest mark :",high)
        print("lowest mark :",low)
        print("avg mark :",avg)
        print("pass students :",pas)
        print("fail students :",fail)

    if o == 8:
        break

