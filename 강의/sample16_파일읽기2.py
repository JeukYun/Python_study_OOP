'''
    c:\sample.txt 파일 예외처리
'''

#예외처리 추가
#### 일반적으로 파일을 읽는 코드

try:
    with open(r"c:\sample2.txt","r",encoding="utf-8")as f: #존재하지 않는 sample2파일 읽기
        while True:
            line = f.readline()
            if not line : break #파일 끝의 비어있는 라인(EOF:End Of File) 을 읽으면 0 이므로 fale로 처리
            print(line, end = "")
except FileNotFoundError as e:
    print("error :",e)
print("정상종료")
