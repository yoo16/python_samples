# calculate
def calculate(x:float)->float:
    y = x + 5
    return y

answer = calculate(2)
print(answer)

# calculateTotalPrice
def calculateTotalPrice(price:int, amount:int)->float:
    tax = 1.1
    totalPrice = price * amount * tax
    return totalPrice

totalPrice = calculateTotalPrice(200, 5)
print(totalPrice)

# calculatePoint
def calculatePoint(price:int, rate:float=0.01)->float:
    point = price * rate
    return point

# 引数を省略
point1 = calculatePoint(totalPrice)

# 引数を指定
point2 = calculatePoint(totalPrice, 0.05)

print(point1)
print(point2)

# str型で定義
def showMessage(message:str):
    print(message)

# str型に、int型をいれられない
# showMessage(10)

def messageTax(item_name:str, price:int, tax_rate:float = 0.1):
    tax = price * tax_rate
    message = f"{item_name}の消費税は{tax}円です。"
    return message

message = messageTax('紅茶', 150)


# move
def move(characterName:str, method:str = "")->str:
    message = ""
    if (method):
        message = f"{characterName}が{method}で移動しています"
    else:
        message = f"{characterName}は家にいます"
    return message

message = move("イヌ", "徒歩")
print(message)

message = move("ネコ")
print(message)

message = move("キリン", "自転車")
print(message)