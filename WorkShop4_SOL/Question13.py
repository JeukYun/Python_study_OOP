
def main():
    '''
       1.입력으로 제공되는 0보다 큰 두 수 사이의 모든 짝수의 합을 계산하는 프로그램을 작성하시오.
        (단, 계산 시 두 수를 포함한다.
        예) 두 수가 4, 8이면 4, 8사이의 짝수는 4, 6, 8이고 짝수합은 18이다.)

    입력1) 25, 40
    출력1) 264
    입력2) 3, 125
    출력2) 3904

    '''
    # 입력 : 두 수
    n1, n2 = 25, 40
    n1, n2 = 3, 125

    total = 0;
    for i in range(n1, n2 + 1):
        if i % 2 == 0:
            total = total + i

    print("-------------------------------------------------------------------------------")
    print("두 수 사이의 짝수합 : ", total)
    print("-------------------------------------------------------------------------------")

# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
