# exam2.py
# 역할 : module1.py 접근하여 연동하는 파일

# 경로지정 방법
# 1) import 패키지명.모듈명
# 2) import 패키지명.모듈명 as 별칭
import sample1.module1 as x

#관례적으로 항상 시작해야되는 모듈에 지정한다.
if __name__ == '__main__':
    print(x.num)
    x.fun()
    c = x.Person()
