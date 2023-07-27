

# 이스케이프 문자 (escape 문자) : \는 특별한 의미를 갖는다.
print("c:\\temp") # 파일 경로 지정시 주로 사용됨.
print("Hello\nworld") # 엔터 친 효과
print("Hello\tworld") # 탭 키 누른 효과
# 따옴표 출력할 때
print("\'")
print("\"")

print("she\'s")
print("\"hello ~!!\"")

#raw string : 이스케이프 문자를 무시한다.
#> 정규표현식(regular expression) : 패턴 매칭, *?-^() 등이 특별한 의미를 가질 때
print(r"c:\\temp") # c:\\temp
print(r"Hello\nworld") # Hello\nworld
print(r"Hello\tworld") # Hello\tworld
print(r"\'") # \'
print(r"\"") # \"
print(r"she\'s") # she\'s
print(r"\"hello ~!!\"") # \"hello ~!!\"