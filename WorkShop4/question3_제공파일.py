
def main():
    '''
       사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라.
       단 값의 범위는 0~255이다. 0보다 작은 값이되는 경우 0을 출력해야 한다

        >>  입력값: 200
        	출력값: 180
	    >>  입력값: 15
	        출력값: 0
    '''

    s = input("입력:")
    ####### 구현 시작 ################
    s = int(s) -20
    if s < 0:
        s = 0

    ########구현 끝 #######################

    print("-------------------------------------------------------------------------------")
    print("출력값: ", s)
    print("-------------------------------------------------------------------------------")


# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
