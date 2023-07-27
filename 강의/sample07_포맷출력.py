# 2) 포맷지정 출력

# 1. 문자열 데이터 표현 (추천 출력 방식)
mesg = "이름:{}".format('홍길동')
print(mesg)

mesg = '이름:{0}'.format('홍길동')
print(mesg)

mesg = '이름:{0}, 나이:{1}'.format('홍길동',20)
print(mesg)

mesg = '이름:{0:5s}, 나이:{1}'.format('홍길동',20) # >> 5s : str
print(mesg)


# 2. 수치 데이터 표현
mesg = '{0}'.format(123456789)
print(mesg)

mesg = '{0:f}'.format(123456789) # 123456789.000000 >> f : float 실수
print(mesg)

mesg = '{0:.3f},{0:.9f}'.format(123.4567) # 123.457 > 소수점 3자리 ,123.456700000 > 소수점 9자리
print(mesg)

mesg = '{0:,}'.format(123456789) # 123,456,789 > 3자리마다 쉼표
print(mesg)

# 3. key 사용 (중요)
mesg = '이름: {username}, 나이: {age}'.format(username='홍길동', age=20)
print(mesg)

# 4. unpacking - 문자열/리스트 >> 집합형을 풀어헤치는 것
                              # 앞에 * 삽입 // dict형식은 ** 두개 사용
mesg = '{0}:{1}:{2}'.format(*'홍길동')
print(mesg)  # 홍:길:동

mesg = '{0}:{1}:{2}'.format(*['홍길동', '이순신', '강감찬'])
print(mesg) # 홍길동:이순신:강감찬

# 4. unpacking - dict
person = {'username': '홍길동', 'age': 20} # ==> username : 홍길동 / age : 20
mesg = '이름: {username}, 나이: {age}'.format(**person)
print(mesg)

#정렬, 채우기, ....
help('FORMATTING')

# 5. % 지정 방식 ( 고전방식 : 잘 사용되지는 않음)  %d > 정수 / %s > 문자 / %f 실수 ....
print("이름: %s 나이: %d 신장: %.2f 결혼여부:%s 성별:%c"
       % ("홍길동", 200, 178.5987, True, '남'))
  #### 출력 결과 : 이름: 홍길동 나이: 200 신장: 178.60 결혼여부:True 성별:남


# 6. format string 방식
name = "KyIN"
age = 20

print("이름:{name} 나이:{age}")
print(f"이름:{name} 나이:{age}")
print(f"이름:{name} 나이:{age+1}") # 산술연산 가능
print(f"이름:{name} 나이:{age > 30}") # 비교연산 가능
print(f"이름:{name.lower()} 나이:{age > 30}")
