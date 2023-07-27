### 변수 ###

# 1) 기본
num = 4
name = "홍길동"
address = "서울"
height = 174.2
isMarried = True
email =["aa@daum.net","bb@google.com"]
info ={
    "핸드폰":["010", "011"],
    "애완동물":["강아지","고양이"]
}  # {key : value} : value 에는 일반형/집합형 모두 가능
print(num, id(num)) #140709113284352 (주소값)
print(name, id(name)) #2730172740880 (주소값)
print(address, id(address)) #2730172639280 (주소값)
print(height, id(height)) #2730172639280 (주소값)
print(isMarried, id(isMarried)) #140709106911056 (주소값)
print(email, id(email)) #2730172538624 (주소값)
print(info, id(info)) #2730172488384 (주소값)