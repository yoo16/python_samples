import math
import numpy as np

message = "東京の天気は晴れです"
keyword = "東京"

index = message.find(keyword)
print(keyword, index)

keyword = "晴れ"
index = message.find(keyword)
print(keyword, index)

keyword = "雨"
index = message.find(keyword)
print(keyword, index)

before = "東京"
after = "横浜"
message = message.replace(before, after)
print(message)

csv = "Apple,Grape,Orange"
foods = csv.split(",")
print(foods)
print(foods[0])

name = " 東京 太郎 "
name = name.strip(" ")
print(name)

message = "My name is {} and I am {} years old.".format(name, 30)
print(message)

data1 = 10
data2 = "Hello"
data3 = [1, 2, 3]

result = isinstance(data1, int)
print(result)

result = isinstance(data1, str)
print(result)

result = isinstance(data2, str)
print(result)

result = isinstance(data3, (list, tuple))
print(result)


value = 16
result = math.sqrt(value)
print(result)

values = [90, 86, 72]
array = np.array(values)
size = array.size
print("count:", size)

total = array.sum()
print("total:", total)

mean = array.mean().round()
print("mean:", mean)


message = ""
user_name = ""
if len(user_name) == 0:
    print("ユーザ名を入力してください")