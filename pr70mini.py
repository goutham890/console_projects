#Q12 — Student Records
#Create student records containing:
#Name
#Age
#Course
#Marks
#Store multiple students.
#Finally display:
#All student records
#Oldest student
#Youngest student
#Topper
#Average marks
#Passed students
#Failed students

age = 0
agey = 100
mark = 0
top = ""
total = 0
students = []
pas = 0
fail = 0

l = int(input("enter the number of students :"))

for i in range(l):
    n = input("enter the name of the student :")
    a = int(input("enter the age of student :"))
    c = input("enter the course of the student :")
    m = int(input("enter the mark of student :"))

    students.append({
        'name': n,
        'age': a,
        'course': c,
        'marks': m
    })

    total = total + m

avg = total / l

print("............................................")

for i in range(len(students)):
    print("name:", students[i]['name'])
    print("age:", students[i]['age'])
    print("course:", students[i]['course'])
    print("mark:", students[i]['marks'])
    print("..........................................")

for i in range(len(students)):

    if students[i]['age'] > age:
        age = students[i]['age']

    if students[i]['age'] < agey:
        agey = students[i]['age']

    if students[i]['marks'] > mark:
        mark = students[i]['marks']
        top = students[i]['name']

    if students[i]['marks'] >= 40:
        pas = pas + 1
    else:
        fail = fail + 1

print("Oldest age:", age)
print("Youngest age:", agey)
print("Topper:", top)
print("Average:", avg)
print("Pass count:", pas)
print("Fail count:", fail)