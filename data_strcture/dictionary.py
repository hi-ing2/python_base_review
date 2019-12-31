# dictionary == dict() == {}

x = {
    "name": "희수",
    "age" : 20,
    2 : "숫자"
}

print(x["name"])
print(x["age"])

print("age" in x)
print(x.keys()) #모든 키
print(x.values()) #모든 벨류

for key in x:
    print("key : " + str(key))
    print("vlaue : " + str(x[key]))

x[0] = "희준" #0이란 키에 희준이란 value를 새로 넣음
x["age"] = 40 #age란 키에 40이란 value로 변경
print(x)