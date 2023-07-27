a = range(1,10,2)
r = range(1,4)
print(list(a))

for idx, i in enumerate(a):
    print(idx, "hello")

for idx, n in enumerate([10,20,30], 1):
    print(idx, n)

b = {"옵치" : "맥크리", "롤" : "렝가", "크아" : "다오"}
print(type(b.items()))
#for a, b in b.items():
#    print(a, b)

print("-------------------------------------")

datas = [1, 2, 3, 4, 5]
for i in datas:
    if i == 3: continue
    if i == 4: break
    print(i, end=' ')
print("end")
##################################################
n1, n2 = 25, 40
x = range(n1,n2)
p = list()

for i in x:
    if i % 2 == 1 : continue
    print(i, end = " ")
    p.append(i)
print()
print(p)

print(sum(p))
print("-------------------------------------")
#################################################

a = [n+1 for n in [1,2,3,4]]
a = [n for n in [1,2,3,4,5,6,7] if n % 2 ==0]
#a = [n%2==0 for n in [1,2,3,4]]
print(a)
print("-------------------------------------")
#################################################

# 가.
x = {"대한민국":"서울", "미국":"워싱턴","중국":"베이징"}
x2 = { v:k for k,v in x.items()}
x2 = { k:len(v) for k,v in x.items()}
print(x2)

# 나.  국가명이 2글자인 경우에만 반환
x2 = {k:v for k,v in x.items() if len(k)==2}
print(x2)

# 다.  국가명중에서  대한민국은  korea로 표시
x2 = {"korea"  if k == "대한민국" else k for k,v in x.items()}
print(x2)

