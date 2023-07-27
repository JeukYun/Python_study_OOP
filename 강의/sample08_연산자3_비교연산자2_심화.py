# 동등 비교
a = [1,2,3,4,5]
b = a

'''
a == b : a와 b의 실제값을 비교한다.
a is b : a와 b의 주소값을 비교한다.
'''

print(a, id(a))
print(b, id(b)) # a, b 모두 같은 주소값을 가진다. / 2160184323904

print(a == b) #True
print(a is b, id(a) == id(b)) #True True

c = a[:] # a의 복사본 생성
print(c, id(c)) # a, b와 다른 주소값을 가진다. / 2160184588608
print(a==c) #True
print(a is c) #False
