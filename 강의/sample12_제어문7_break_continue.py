'''
   break: 반복문 빠져나올때
   
   continue: 특정 회차에서 일부분의 문장을 skip 할때

'''

# break, continue , else 문
datas = [1, 2, 3, 4, 5]
print("-------------------------------------")
for i in datas:
    if i == 3: continue # 3을 건너 뛰고 다시 첫번째 fot문으로 이동 (3인 경우 출력하지 않음)
    # if i == 4: break
    print(i, end=' ')
print("end")

for i in datas:
    if i == 4: break
    print(i, end=' ')
else:
    print("정상종료") # break가 아닌 정상적으로 반복된 경우에만 실행됨.
print("end")