students = {
    "Peter": 80,
    "Tony": 65,
    "Cap": 92,
    "Hulk": 45,
    "Thor": 75
}
n = 0
p = 100
y = []
for i in students:
    y = students.values()
    if y[i] > n:
        n = y[i]
    if students[i] == n:
        print("top",student[i])
    if y[i]<p:
        p = y[i]
    if student[i] == p:
        print(i)