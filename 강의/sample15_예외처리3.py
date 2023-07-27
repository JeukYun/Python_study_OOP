'''
    예외처리
'''

print("1")
print("2")

try:
    n = 0
    result = 10/n
    print("결과값:", result)
#except ZeroDivisionError as e:
except Exception as e: # 적합한 예외 클래스를 지정해야한다.
                       # 단 부모 예외클래스 지정가능 (다형성 특징)
                       # 다형성을 이용해서 모든 예외를 Exception으로 사용 가능하나 권장x, 디테일하게 처리함을 권장
    print("0으로 나누어 예외 발생됨")

print("3")
print("end.정상종료")
