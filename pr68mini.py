#Q10 — Student Performance System
#Ask for N students.
#For each student:
#Name
#Marks
#Finally display:
#All students
#Highest mark
#Lowest mark
#Average
#Pass count
#Fail count
#Topper's name
#Students above average

n = int(input("enter the number :"))
x = {}
i = 0
high = 0
low = 100
total = 0
pas = 0
fail = 0
while(i<n):
    p = input("enter the name :")
    m = int(input("enter the mark :"))
    x[p] = m
    i = i + 1
for j in x:
    mark = x[j]
    if mark >high:
        high = mark
    if mark < low:
        low = mark
    total = total + x[j]
    if x[j] >= 40:
        pas = pas + 1
    if x[j]< 40:
        fail = fail + 1
    if x[j] == high:
        k = j
avg = total / len(x)

print(x.keys())
print("highest :",high)
print("lowest :",low)
print("average :",avg)
print("pass :",pas)
print("fail :",fail)
print("top student :",k)
for w in x:
    if x[w]>avg:
        print("Students above average :",w)

