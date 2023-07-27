'''
    상속후
'''
##############################################################
# 공통적인 속성 및 동작 추출하여 큰 개념의 Pet 작성
class Pet: # 자동으로 object가 상위 클래스로 지정된다.
    def __init__(self, n, a):
        self.username = n
        self.age = a

class Cat(Pet): # 상속 // Cat is a Pet (상속 관계는 이지어 관계)
    def __init__(self, n, a):
        super().__init__(n,a)  #부모에서 초기화 하도록 코드 수정
    def info(self):
        return self.username, self.age

class Dog(Pet): # 상속 시 (부모 명) 필수
    def __init__(self, n, a, g):
        super().__init__(n,a)
        self.gender = g # gender는 부모class에 없으므로 dog에서 초기화

    def info(self):
        return self.username, self.age, self.gender


#################################################
c = Cat("야옹이",2)
d = Dog("망치",1,"수컷")

print("고양이", c.info())
print("강아지", d.info())



# 상속의 계층구조 확인 : 클래스명.mro
print(Cat.mro()) #[<class '__main__.Cat'>, <class '__main__.Pet'>, <class 'object'>]
                 #             cat -> pet -> object

# 다중상속 지원
