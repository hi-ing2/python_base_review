from class_basic import Person #왜 person 클래스만 호출하는게아니라 전부다 호출을 시키는가? 질문하기

class Police(Person): #폴리스는 펄슨을 상속
    def arrest(self, to_arrest):
        print("넌 체포됐다, " + to_arrest)

class Programmer(Person):
    def program(self, to_program):
        print("다음엔 뭘 만들지? 아 이걸 만들어야 겠다. " + to_program)

hesu = Person("희수", 50)
hesu.introduce("바보") #class_basic의 hesu와 다르게 지역변수 취급
han = hesu.say_hello("한이")

dohan = Police("김두한", 50)
dohan.say_hello("시라소니") #class_basic의 say_hello도 호출 가능 (상속)
dohan.arrest("시라소니")


siyoung = Programmer("시영", 45)
# siyoung.arrest(..) : 불가능
siyoung.program("캘린더 어플!")