import random

numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total += number
print(total)

for x in range(3):
    for y in range(3):
        plot = str(x) + "-" + str(y)
        print(plot)

drinks = ["コーヒー", "紅茶", "ほうじ茶"]
for index, drink in enumerate(drinks):
    message = str(index) + ":" + drink
    print(message)

count = 0
while count <= 10:
    count += 1
print(count)

count = 0
while True:
    count += 1
    if (count == 5):
        print("Finish!")
        break
print(count)

items = ["PC", "TV", "エアコン"]
for item in items:
    print(item)

for x in range(1, 10):
    for y in range(1, 10):
        print(x * y, end=" ")
    print("")

marks = ["⚫︎", "⚪︎︎"]
for x in range(0, 5):
    print("|", end="")
    for y in range(0, 5):
        index = random.randint(0, 1)
        print(marks[index], end="|")
    print("")
