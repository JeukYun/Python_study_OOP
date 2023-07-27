
def main():
    '''
  	List comprehension을 사용하여 입력된 리스트중에서 0th,4th, 5th 값을 제거하고 출력하는 코드를 작성하시오.

    입력: [12,24,35,70,88,120,155]
    출력: [24, 35, 70, 155]




    '''
    input_data = [12,24,35,70,88,120,155]
    output_data = []

    output_data = [x for (i,x) in enumerate(input_data) if i not in (0,4,5)]

    print("-------------------------------------------------------------------------------")
    print(output_data)
    print("-------------------------------------------------------------------------------")

# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
