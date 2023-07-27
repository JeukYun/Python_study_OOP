'''
    c:\sample.txt 파일 읽기
'''

# 1. 파일읽기
# mode : r(읽기) w(쓰기, 덮어쓰기) a(쓰기, 추가)

# 가. f.read() 는 한번에 str반환한다.
with open(r"c:\sample.txt","r",encoding="utf-8")as f:
    contents = f.read()
    print(contents)

print("#"*100)

# 나. f.readline() 은 첫줄만 읽어옴.
with open(r"c:\sample.txt","r",encoding="utf-8")as f:
    line = f.readline()
    print(line)

print("#"*100)

# 다. f.readline() ==> 반복해서 읽어옴.  : 일반적으로 파일 읽는 코드
with open(r"c:\sample.txt","r",encoding="utf-8")as f:
    while True:
        line = f.readline()
        if not line : break #파일 끝의 비어있는 라인(EOF:End Of File) 을 읽으면 0 이므로 fale로 처리
        print(line, end = "")

print("#"*100)

# 라. f.readlines() 는 한번에 list 반환한다.
with open(r"c:\sample.txt","r",encoding="utf-8")as f:
    line = f.readlines()
    print(line)

print("#"*100)

# f.readlinea() ==> 한줄씩 읽기
with open(r"c:\sample.txt","r",encoding="utf-8")as f:
    list_line = f.readlines()
    print(list_line)
    for line in list_line:
        print(line, end ="")


