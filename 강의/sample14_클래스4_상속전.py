'''
    상속전
'''
##############################################################
class Cat: # 생성자
    def __init__(self, n, a): #인스턴스 변수
        self.username = n
        self.age = a

    def info(self):  #메서드
        return self.username, self.age


class Dog:  # 생성자
    def __init__(self, n, a, g):  # 인스턴스 변수
        self.username = n
        self.age = a
        self.gender = g

    def info(self):  # 메서드
        return self.username, self.age, self.gender


#################################################
c = Cat("야옹이",2)
d = Dog("망치",1,"수컷")

print("고양이", c.info())
print("강아지", d.info())