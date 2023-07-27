'''
    c:\sample2.txt 파일 쓰기
    => 파일이 없는 경우 자동으로 생성해준다.
'''
# "w":덮어쓰기 // "a":추가
with open(r"c:\sampel2.txt","w", encoding="utf-8") as f:
    f.write("python pandas numpy")
print("end. 정상종료")

