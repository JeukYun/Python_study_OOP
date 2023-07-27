'''
    메서드

    - 문법 :
           class 클래스명 :

              #생성자 ==> 인스턴스 변수 값 초기화 담당
              def __init__(self):
                    self.변수명 = n   # 인스턴스 변수 ==> 값 저장 담당

              # method ==> 일반적인 기능처리 담당
              def 메서드명(self):
                  pass
'''
##############################################################
# 기본적인 class 구성
class Cat:
    # 생성자
    def __init__(self, n, a):
        # 인스턴스 변수
        self.username = n
        self.age = a

    # method
    def setage(self,n):
        self.age = n

    def getage(self):
        return self.age


# 실제 고양이(인스턴스)

c = Cat("야옹이",2)
print(c.username, c.age)
print(c.username, c.getage())

c2 = Cat("삐약이",3)
print(c2.username, c2.age)
print(c2.username, c2.getage())