
def main():
    '''
       주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다.
       주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라


지역코드	출생지
------------
00 ~ 08	서울
09 ~ 12	부산



       > 주민등록번호: 821010-1635210

         서울이 아닙니다

    '''
    a = [0,1,2,3,4,5,6,7,8]
    reg_num = input("주민등록번호:")
    mesg = None
    ####### 구현 시작 ################
    if int(reg_num[7:9]) in a:
        mesg = "서울"
    else :
        mesg = "서울이 아닙니다."

    ########구현 끝 #######################

    print("-------------------------------------------------------------------------------")
    print(mesg)
    print("-------------------------------------------------------------------------------")
# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
