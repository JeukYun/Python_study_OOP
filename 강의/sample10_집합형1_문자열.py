#########################################################################
### 집합형 데이터 ###########################################################
#########################################################################

#1. 문자열 생성 방법
s = 'sequence'
s = '''sequence'''
s = """sequence"""
s = str(10)

s = "sequence" # 주로 사용 됨

# triple 사용용도 : 정형화된 문자열 처리 >> 라인변경 가능
s2 = """
    <html>
      <body>
        <p>
"""
print(s2)

# 일반적으로 사용 시 역슬래시 사용
s2 = "<html>" \
     "<body>" \
     "<p>"\



#2. 문자열 함수
# 문자열은 str객체 관리한다.
s = "sequence"
print(type(s)) # <class 'str'>

# str객체에 어떤 함수가 있는지 확인, 사용 시 반드시 문자열.함수명 형식을 이용(중요)
print(dir(str))
'''
['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 
'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 
'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 
'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 
'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
'''

print("1. 문자열 길이:", len(s)) # 8  >> len은 __builtins__
print("2. 특정문자 포함횟수:", s.count('e')) # 3
print("3. 소문자로:", "HeLLo".lower()) # hello
print("4. 대문자로:", "HeLLo".upper()) # HELLO
print("5. swap 문자로:", "HeLLo".swapcase()) # hEllO > 소문자, 대문자 변환
print("6. 공백제거 및 특정문자 제거:\n") # sql의 Ltrim, rtrim, trim 기능과 유사
print("    HeLLo    ".lstrip()) # HeLLo   >> 왼쪽 날리기
print("HHeLLH".lstrip("H")) # eLLH
print(len("    HeLLo    ".lstrip())) # 9
print("    HeLLo    ".rstrip()) #    HeLLo  >> 오른쪽 날리기
print("HHeLLHH".rstrip("H")) # HHeLL
print("    HeLLo    ".strip()) #
print("HHeLLHH".strip("H")) # eLL
print(len("    HeLLo    ".strip())) # 5

print("7. 문자열 변경:", "HeLHO".replace('H', 'A')) # AeLAO
print("8. 구분자:", "aaa/bbb/ccc".split("/")) # ['aaa', 'bbb', 'ccc'] , /를 기준으로 나누어 리스트 형식 출력
print('9. 특정 글자 시작 : ', s.startswith('s'), s.startswith('a')) # True False
print('10. 특정 글자 끝 : ', s.endswith('e'), s.endswith('x')) # True False

print("11. 문자로만 구성?", "대한Heloo".isalpha())  # True
print("11. 문자로만 구성?", "12".isalpha())   # False
print("11. 숫자로만 구성?", "12".isnumeric())   # True

print("12. S.find(sub[, start[, end]]) -> int") # 대괄호는 생략가능함을 뜻함. start, end로 범위 지정 가능
print("12. 검색위치1:", s.find('e')) # 1
print("12. 검색위치2:", s.find('e', 2)) # 4
print("12. 검색위치2-2:", s.find('x', 2)) # -1 >> 값을 찾지 못하면 -1 리턴
print("12. 검색위치3:", s.rfind('e')) # 7 >> 가장 큰 index 값 반환
help(str.find)
help(str.rfind)
help(str.startswith)

print("13. join:", ",".join(["A", "B", "C"])) # A,B,C (중요)
print("13. join:", "와".join(["A", "B", "C"])) # A와B와C  >> 문자열만 가능, 숫지 불가

#sql의 Lpad, rpad 와 비숫한 기능
print("14. center:", "Hello".center(20, "_")) # 20 자리수로 표시하고 _로 마킹
print("15. rjust:", "Hello".rjust(20, "_")) # 20 자리수로 표시하고 _로 마킹
print("16. ljust:", "Hello".ljust(20, "_")) # 20 자리수로 표시하고 _로 마킹
print("17. capitalize:", "heLLOX".capitalize()) # 첫글자 대문자

print("18. 멤버쉽 연산자1:", "H" in "Hello") # True
print("19. 멤버쉽 연산자2:", "X" in "Hello") # False

#문자열 종류
'''
s = "hello" ==>> unicode string, text 기반 , 일반적으로 사용하는 문자열
s2 = b"hello" ==>> bytes string, binary 기반 , 네트워크 이용한 경우에는 bytes string으로 처리된다.
'''
# 1) unicode --> bytes ( 암호화 작업 : encode 함수 )
s = "hello안녕하세요"
s2 = s.encode('utf-8')
print(s, s2)
# help(str.encode)
# 2) bytes --> unicode ( 복호화 작업 : decode 함수 )
#print(dir(bytes))
'''
'capitalize', 'center', 'count', 'decode', 'endswith',
 'expandtabs', 'find', 'fromhex', 'hex', 'index',
  'isalnum', 'isalpha', 'isascii', 'isdigit', 'islower', 'isspace', 
  'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
  'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 
  'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 
  'title', 'translate', 'upper', 'zfill']
'''

s3 = s2.decode('utf-8')
print(s2, s3)

# 2. 문자열 인덱싱과 슬라이싱
m = "대한민국"
'''
    -4 -3 -2 -1
     대 한 민 국
     0  1  2 3
'''
# 1) 인덱싱(indexing)
print("1:", m[0])  #  대
print("2:", m[-1]) #  국

# 2) 슬라이싱
'''
 m[start : end : step]
 start : 시작 idx 값, 생략 시 맨 처음
 end : 끝 idx 값, end 값 미포함, 생략 시 맨 끝
 step : 기본값 1
'''
print("3:", m[0:3]) # 대한민
print("4:", m[1:]) # 한민국
print("5:", m[:2]) #  대한
print("6:", m[-3:-1]) # 한민
print("7:", m[-3:]) #  한민국
print("7:", m[:-1]) #  대한민
print("8:", m[0:3:2]) #대민
print("9:", m[:])   #대한민국
print("11:", m[::-1])    # 국민한대 >>> 거꾸로 출력
print("11:", m[::-2])    # 국한
print("10:", m*2)    #대한민국대한민국
