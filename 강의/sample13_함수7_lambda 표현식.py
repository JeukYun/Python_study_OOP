'''
    Lambda 표현식 (익명함수)
    - def 함수명() 문법을 이용한 함수 작성의 또 다른 표현식이다.
    - 반드시 단일 문장인 경우에만 Lambda 표현식이 가능하다.
    - 익명함수이기 때문에 변수에 저장해서 호출해서 사용. (일급객체이기 때문에 가능)
'''

#1. 파라미터x 리턴값x
def fun():
    print("fun")

# Lambda 표현식
fun = lambda : print("lambda fun")
fun()

#2. 파라미터 o, 리턴 x
def fun2(n=10,n2=20, *n3, **n4): # n 에 defalt 값 지정 가능
    print("fun2",n ,n2)

# Lambda 표현식
fun2 = lambda n = 10, n2 = 20, *n3, **n4 : print("lambda fun2", n, n2, n3, n4) # n 에 defalt 값 지정 가능
fun2(10, 20)
fun2()
fun2(10,23,4,4,5,6,5, age =20, addr= "서울")

#3. 파라미터 x 리턴값 o
def fun3():
    return 100

# Lambda 표현식
fun3 = lambda : 100

result = fun3()
print("lamda fun3", result)

#4. 파라미터 o, 리턴 o
def fun4(n, n2):
    return n+n2
# Lambda 표현식
fun4 = lambda n, n2 : n+n2

result = fun4(10,30)
print("lamda fun4", result)