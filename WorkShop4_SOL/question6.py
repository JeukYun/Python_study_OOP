
def main():
    '''
       아래와 같이 fruit 딕셔너리가 정의되어 있다.
       사용자가 입력한 값이 딕셔너리 값 (value)에 포함되었다면
       "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
    '''

    fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
    mesg = None
    user_in = input("좋아하는과일은?")

    if user_in in fruit.values():
        mesg="정답입니다"
    else:
        mesg="오답입니다"

    print("-------------------------------------------------------------------------------")
    print(mesg)
    print("-------------------------------------------------------------------------------")


# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
