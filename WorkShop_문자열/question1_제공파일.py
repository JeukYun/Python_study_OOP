
def main():
    '''
        입력으로 제공되는 주민번호 뒷자리의 첫번째 숫자를 이용하여 성별을 판별하는 프로그램을 작성하시오.
        (성별 기준, 남(M): 1 또는 3, 여(F): 2 또는 4)
        입력 예시1) 900103-1******, 출력 예시1) M
        입력 예시2) 070809-4******, 출력 예시2) F
    '''


    # 입력 : 주민번호 데이터
    jumin = "800103-1******"
    # jumnin = "050809-4******"
    gender = None

    ####### 구현 시작 ################


    ########구현 끝 #######################

    print("-------------------------------------------------------------------------------")
    print("성별은 : ", gender)
    print("-------------------------------------------------------------------------------")


# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
