
def main():
    '''
       우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다.
       예를들어, 강북구의 경우 010, 011, 012 세 자리로 시작한다.

-	 0	      1	      2	      3	      4	      5 	  6	      7	      8 	 9
01	강북구	강북구	강북구	도봉구	도봉구	도봉구	노원구	노원구	노원구	노원구


     사용자로 부터 5자리 우편번호를 입력받고 구를 판별하라


       > 우편번호: 01400

         도봉구

    '''

    zipcode = input("우편번호:")
    mesg = None
    ####### 구현 시작 ################
    if zipcode[2:3] == "0" :
        mesg = "깅북구"

    ########구현 끝 #######################

    print("-------------------------------------------------------------------------------")
    print(mesg)
    print("-------------------------------------------------------------------------------")
# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
