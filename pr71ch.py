n = int(input("enter the number :"))
x = {}

for i in range(n):
    p = input("enter word :")

    if p in x:
        x[p] = x[p] + 1
    else:
        x[p] = 1

print(x)