price = 100

# 左項と右項が同じ
isMatch = (price == 100)
print(isMatch)

# 左項が右項より小さいか
isMatch = (price < 100)
print(isMatch)

# 左項と右項が等しくないか
isMatch = (price != 100)
print(isMatch)

# 左項が右項より大きいか
isMatch = (price > 100)
print(isMatch)

# 左項が右項以上か
isMatch = (price >= 100)
print(isMatch)


str1 = "20"
str2 = "20"
number1 = 20
number2 = 30

# String同士の比較
isMatch = (str1 == str2)
print(isMatch)

# int同士の比較
isMatch = (number1 == number2)
print(isMatch)


isActive = True
isMember = False

result = (isActive and isMember)
print(result)

result = (isActive or isMember)
print(result)

result = not isActive
print(result)