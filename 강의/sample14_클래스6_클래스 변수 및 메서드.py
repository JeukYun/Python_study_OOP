'''
    클래스 변수 및 메서드
'''

class Person:

    address = "서울" #클래스 변수, 단 한번 생성(사는곳이 모두 서울이니까)  --> 목적 : 여러 인스턴스가 공유 가능

    def __init__(self, n, a): # 인스턴스 변수, 객체 생성 시 마다 매번 생성(사람마다 속성이 다 다르니까)
        self.username = n
        self.age = a

    def info(self):
         return self.username, self.age, Person.address

    #클래스 메서드 목적 : 객체생성 없이 사용하기 위해
    @classmethod #데코레이트
    def get_address(cls):
        return Person.address

# Person.address = "제주" #실행 시 힌번에 모든  address 변경 가능
p1 = Person("홍길동", 20)
p2 = Person("이순신", 44)

print("p1 :", p1.info())
print("p2 :", p2.info())

print(Person.get_address())

print("p1 :", p1.info(), Person.get_address())
print("p2 :", p2.info(), Person.get_address())

