'''
     경로
'''

import os

#1. 현재 작업경로 출력
print(os.getcwd()) # C:\Users\yju12\PycharmProjects\pythonProject1

#2. 임의의 경로 생성하기 c:\users\xxx
print(os.path.join("c:\\",'Users','xxx'))

# 현재 작업 경로에 aaa.txt 경로 추가 C:\Users\yju12\PycharmProjects\pythonProject1\aaa.txt
print(os.path.join(os.getcwd(),'aaa.txt'))

#3. 특정 경로에서 디렉토리 경로 얻기
p = r"C:\Users\yju12\PycharmProjects\pythonProject1\aaa.txt"
print(os.path.dirname(p)) #C:\Users\yju12\PycharmProjects\pythonProject1

#4. 특정 경로에서 파일명 얻기
p = r"C:\Users\yju12\PycharmProjects\pythonProject1\aaa.txt"
print(os.path.basename(p)) #aaa.txt

#5. 특정 경로에서 디렉토리, 파일명 한번에 분리
p = r"C:\Users\yju12\PycharmProjects\pythonProject1\aaa.txt"
dir, file = os.path.split(p)
print(dir, file)

#6. 파일명에서 파일명과 확장자 분리
p = r"C:\Users\yju12\PycharmProjects\pythonProject1\aaa.txt"
file = os.path.basename(p) #aaa.txt
file_name, extend_name = os.path.splitext(file)
print(file_name, extend_name)

#7 특정 디렉토리 목록 보기
dir_list = os.listdir(os.getcwd())
print(dir_list)