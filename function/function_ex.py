#먼저 이름과 나이를 말해라
#나이가 10살 미만이면 "안녕" 이라고 말해라
#나이가 10살살에서 20살 사이면 "안녕하세요" 라고 말해라
#그 외에는 "안녕하십니까" 라고 말해라

def sayHello(name, age):
    if age <10:
        print("안녕," + name)
    elif age <= 20 & age >= 10:
        print("안녕하세요," + name)
    else:
        print("안녕하십니까," + name)


sayHello("알렉스", 20)
sayHello("스미스", 90)
sayHello("존스", 5)