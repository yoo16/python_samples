answer = 1 + 2
print(answer)

answer = answer + 3
print(answer)

answer = 1 + 2
answer = answer + 3
answer = answer - 2
answer = answer * 5
answer = answer / 2
print(answer)

mod = answer % 3
print(mod)

price = 200
pointRate = 0.05
point = price * pointRate

message = str(point) + "pt"
print(message)


amount = 0

# amount が１増加
amount += 1
print(amount)

# amount が１減少
amount -= 1
print(amount)


amount = 0

price = 110
amount += 3

price -= 10
price *= amount
print(price)


itemName = "コーヒー"
message = itemName + "の価格は" + str(price) + "円です。"
message += "購入しますか？"
print(message)


x = 2 ** 1000
print(x)


# price = 100
# amount = 0
# average = price / amount
# print(average)
