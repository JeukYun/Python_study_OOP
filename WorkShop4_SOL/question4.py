
def main():
    '''
       사용자로부터 입력 받은 시간이 정각인지 판별하라.

       >> 현재시간:02:00
          정각 입니다.
	   >> 현재시간:03:10
	      정각이 아닙니다.
    '''

    user_in = input("현재시간:")
    mesg = None
    if user_in[3:] == "00":
        mesg="정각 입니다"
    else:
        mesg="정각이 아닙니다"

    print("-------------------------------------------------------------------------------")
    print(mesg)
    print("-------------------------------------------------------------------------------")


# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()