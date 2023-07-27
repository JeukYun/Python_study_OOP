# 파이썬은 대소문자를 구별
print("Hello World")
print("Hello World") # ctrl + d : 코드 한줄 복사
print(True, False) # 논리값 (참, 거짓)
print(10, 3.14) # shift + alt + 방향키 : 코드 이동
print(None) # null값 의미

print([10,20,30,20,30]) # 대괄호 [값, ...] : 리스트(list) > 순서 있음, 중복 가능, 값 변경 가능
print((10,20,30,20,30)) # 소괄호 (값, ...) : 튜플(tuple) > 순서 있음, 중복 가능, 값 변경 불가
print({10,20,30,20,30}) # 중괄호 {값, ...} : 셋(set) > 순서 없음, 중복 불가, immutable값만 저장 가능
print({'p01' : 30, 'p02' : 10}) # 중괄호 {key1:value1, key2:value2...} : 딕트(dict)

# 셋(set) > immutable(값변경 불가)자료형 저장 가능 > [값, 값 ..] (리스트)형식 입력 시 오류발생
print({10,20,30,20,30,"홍길동"})
print({10,20,30,20,30,("홍길동","임꺽정")})

