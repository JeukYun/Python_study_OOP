
def main():
    '''
     자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하라

    license_plate = "24가 2210"

    출력:
        2210
    '''
    license_plate = "24가 2210"

    car_num = None
    ####### 구현 시작 ################
    car_num = license_plate[4:9]

    ########구현 끝 #######################

    print("-------------------------------------------------------------------------------")
    print(car_num)
    print("-------------------------------------------------------------------------------")


# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
