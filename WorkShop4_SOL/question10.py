
def main():
    '''
       휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다.
       사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.

번호	통신사
---------
011	SKT
016	KT
019	LGU
010	알수없음


       >> 휴대전화 번호 입력: 011-345-1922

        출력: 당신은 SKT 사용자입니다.
    '''

    phone_number = input("휴대전화 번호 입력 : ")
    mesg = None
    if phone_number[0:3] == "011":
        mesg= "당신은 SKT 사용자입니다."
    elif phone_number[0:3] == "016":
        mesg= "당신은 KT 사용자입니다."
    elif phone_number[0:3] == "019":
        mesg= "당신은 LGU 사용자입니다."
    else:
        mesg= "당신은 알수 없는 사용자입니다."

    print("-------------------------------------------------------------------------------")
    print(mesg)
    print("-------------------------------------------------------------------------------")
# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
