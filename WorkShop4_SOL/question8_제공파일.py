
def main():
    '''
       사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후
       이를 원으로 변환하는 프로그램을 작성하라.
       각 통화별 환율은 다음과 같다.
       사용자는
        100 달러
        1000 엔
        13 유로
        100 위안
       과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다

   통화명   환율
   -------------
   달러	   1167
   엔	   1.096
   유로	   1268
   위안	   171

      >> 입력: 100 달러
         116700.00 원
    '''

    user_in = input("입력:")
    price = None
    ####### 구현 시작 ################


    ########구현 끝 #######################
    
    print("-------------------------------------------------------------------------------")
    print(price, "원")
    print("-------------------------------------------------------------------------------")
# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
