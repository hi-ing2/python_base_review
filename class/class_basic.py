class Person:
    name = "후아유"
    def __init__(self, name, age): #초기화(initialize) 메소드 : 어떤 클래스의 객체가 만들어질 때 자동으로 호출되어서 그 객체가 갖게 될 여러 가지 성질을 정해주는 일 
        self.name= name
        self.age = age
    def say_hello(self, to_name): 
        # print("안녕 ! "+ to_name + "나는 " + Person.name)
        print("안녕 ! "+ to_name + " 나는 " + self.name) #say_hello에 넣을 self.name 가져오고
    def introduce(self, name):
        print ("내이름은" + self.name + "그리고 나는 " + str(self.age)) #introduce에 넣을 self.name 가져옴

class Test:
    hesu = Person("희수", 30) #외부인자값을 Person 클래스에 넣으면 초기화 메소드에 자동으로 대입함(하나의 규칙)
    soyoung = Person("소영", 20) #Person class __init__에 (이름, 나이) 등록

    hesu.introduce("바보") #hesu로 정의 된 클래스의 introduce 옵젝 발동
    soyoung.say_hello("희수") #soyoung으로 정의 된 클래스의 say_hello 옵젝 발동 
    

class a:
    print("a")
    print("-------구분선--------")