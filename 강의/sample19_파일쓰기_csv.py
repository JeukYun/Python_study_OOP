'''
    c:\sample6.csv 파일 쓰기
'''
import csv

#가. 한 줄 작성
with open(r"c:\sample6.csv",mode = "w",encoding="utf-8")as f:
    data = csv.writer(f)
    data.writerow(["홍길동2",20,"서울2"]) #집합형 데이터만 가능
                                        #계속 실행시 덮어쓰기 됨

#나. 여러줄 작성
with open(r"c:\sample7.csv",mode = "w", newline="", encoding="utf-8")as f: #옵션에 newline="" 추가시 여러줄 작성 시 엔터 x
    data = csv.writer(f)
    data.writerows([["홍길동1",50,"서울1"], ["홍길동2",20,"서울2"]])


print("end, 정상종료")
