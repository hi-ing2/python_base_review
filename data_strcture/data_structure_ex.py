fruit = ["사과", "바나나", "키위", "복숭아", "바나나", "복숭아", "복숭아", "키위"]

d = {}

for f in fruit: #list fruit의 값을 f에 대입
    if f in d: #d라는 딕셔너리에 f가 들어잇어?
        d[f] = d[f] + 1 #d라는 딕셔너리에 f가 있으면 value(개수) 1 증가
    else:
        d[f] = 1 #d라는 딕셔너리에 f가 없으면(아니면) value를 1로 지정후 new dict 생성

print(d)
print(d["사과"])
