def main():
    '''
   icecream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라

    출력: 6700
    '''
    icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

    total_price = None
    
    ####### 구현 시작 ################
    price = (v for k, v in icecream.items())
    total_price = sum(price)
    ########구현 끝 #######################

    print("-------------------------------------------------------------------------------")
    print("금액총합 : ", total_price)
    print("-------------------------------------------------------------------------------")


# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
