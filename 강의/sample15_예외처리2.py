'''
    예외처리
'''

print("1")
print("2")

try:
    n = 0
    result = 10/n
    print("결과값:", result)
except ZeroDivisionError as e: # 적합한 예외 클래스를 지정해야한다.
    print("0으로 나누어 예외 발생됨")

print("3")
print("end.정상종료")
