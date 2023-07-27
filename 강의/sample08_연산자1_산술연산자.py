### 연산자 ###

# 1) 산술 연산자
a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print("h"*10) # hhhhhhhhhh
print(a/b)    # 3.3333333333333335  : 나누기 시 소수점까지 출력됨.
print(a % b)  # 1  ,  Modulus

print(a//b)   # 3  ,  Floor Division   : 몫만 출력 / 소수점 버림
print(a**b)   # square ( 제곱 )

# 몫, 나머지를 한번에 반환 해주는 함수 (builtins 객체)
result = divmod(10,3)
print(result) # 결과 : (3, 1) >> 튜플로 반환됨

x, y = divmod(10, 3) # >> x, y 동시 반환
print(x, y) # 일반적으로 사용 >> 결과 : x y 각 3, 1 반환
# 예시 >> #name, age, address = ( "홍길동", 20, "서울")

