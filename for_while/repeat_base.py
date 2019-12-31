# print("철수: 안녕 영희야 뭐해")
# print("영희: 안녕 철수야 걍 있어")
# print("철수: 안녕 영희야 뭐해")
# print("영희: 안녕 철수야 걍 있어")
# print("철수: 안녕 영희야 뭐해")
# print("영희: 안녕 철수야 걍 있어")
# print("철수: 안녕 영희야 뭐해")
# print("영희: 안녕 철수야 걍 있어")
# print("철수: 안녕 영희야 뭐해")
# print("영희: 안녕 철수야 걍 있어")
# print("철수: 안녕 영희야 뭐해")
# print("영희: 안녕 철수야 걍 있어")
# 5번 반복

for i in range(5):
    print(i)
    print("철수: 안녕 영희야 뭐해")
    print("영희: 안녕 철수야 걍 있어")

j = 0
while j < 3: #기본 while 보다는 if와 반복문 결합한 원리
    print(j) 
    print("철수: 안녕 영희야 뭐해")
    print("영희: 안녕 철수야 걍 있어")
    j += 1

j = 0
#break, continue
while True:
    print(j) 
    print("철수: 안녕 영희야 뭐해")
    print("영희: 안녕 철수야 걍 있어")
    j += 1
    if j > 2:
        break # 조건에 만족하면 반복문 끝내라
j = 0
#break, continue
while True:
    print(j) 
    print("철수: 안녕 영희야 뭐해")
    print("영희: 안녕 철수야 걍 있어")
    j += 1
    if j > 2:
        break # 조건에 만족하면 반복문 끝내라

j=0
for j in range(10):
    print(j) 
    print("철수: 안녕 영희야 뭐해")
    print("영희: 안녕 철수야 걍 있어")
    if j > 5:
        continue
    print("희수 : 여러분 안녕") # 해당 프린트문은 if소속이 아니라 continue 소속