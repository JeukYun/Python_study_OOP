
# 3) 변수 타입 체크
#일반형 데이터
a = 10  # <class 'int'>
b = 3.14 # <class 'float'>
c = True # <class 'bool'>
x = None # <class 'NoneType'>
y = lambda : print("hello") # <class 'function'> 함수 > def와 동일 / 형태만 다름

#집합형 데이터
d = [10, 20, 30] # <class 'list'>
e = (10, 20, 30) # <class 'tuple'>
f = {10, 20, 30} # <class 'set'>
g = {'key': 100} # <class 'dict'>

# 문자열 종류 2가지
# "hello" : unicode 문자열 또는 b"hello" : byte 문자열
h = "hello"     # <class 'str'> unicode string
h2 = b"hello"   # <class 'bytes'> byte string ==>> web에서 문자열을 가져올 때 (크롤링 할 때)

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(c, type(x))
print(c, type(y))

print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))
print(h, type(h))
print(h2, type(h2))

## 비교
print(isinstance(a, int)) # >>True
print(isinstance(a, str)) # >>False