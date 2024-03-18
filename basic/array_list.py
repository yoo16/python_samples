import random

drinks = ()
drinks = ("") * 3
drinks = ("コーヒー", "紅茶", "ほうじ茶")
print(drinks)

selectDrink = drinks[1]
print(selectDrink)

strings = [""] * 3

drinks = ["コーヒー", "紅茶", "ほうじ茶"]
print(drinks)

selectDrink = drinks[1]
print(selectDrink)

drinks[1] = "ウーロン茶"
print(drinks)

numbers = [0] * 3
numbers[0] = 55
numbers[1] = 31
numbers[2] = 72
# numbers[3] = 50

print(numbers)

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers = numbers1 + numbers2
print(numbers)

numbers *= 3
print(numbers)

# ランダムな整数を生成
index = random.randint(0, 2)
hands = ("グー", "チョキ", "パー")
print(hands[index])