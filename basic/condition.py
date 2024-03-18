price = 300
money = 500
message = ""

if money > 0 and price > 0:
    if money >= price:
        message = "お買い上げありがとうございました"
    else:
        message = "購入金額が足りません"
else:
    message = "入力が間違っています"
print(message)

score = 100
if (score > 0):
    if score >= 90:
        print("優")
    elif score >= 70:
        print("良")
    elif score >= 50:
        print("可")
    else:
        print("不可")