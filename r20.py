scores = {
    "Peter": 80,
    "Tony": 65,
    "Cap": 92,
    "Hulk": 45,
    "Thor": 75
}

total = 0

for i in scores:
    total = total + scores[i]

average = total / len(scores)

count = 0
above_average = []

for i in scores:
    if scores[i] > average:
        count = count + 1
        above_average.append(i)

print("Average:", average)
print("Above Average:", count)
print("Students:", above_average)