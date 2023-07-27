# 2. 딕트(dict)
# 1) 딕트 ( dict ) 생성 : immutable한 키와 mutable한 값으로 구성
m0 = {} # >> dict
m1 = dict()
m2 = {'name':'홍길동1','age':20} #일반적인 dict 생성 방법
m3 = dict(name='홍길동2', age=20)
print(m0, m1, m2, m3)

# 2) 딕셔너리 함수 ('items', 'keys', 'values' 3가지 중요)
'''
['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 
'pop', 'popitem', 'setdefault', 'update', 'values']
'''

# (1) dict 추가
coffee = {'espresso':'에스프레소', 'latte':'라떼'}
print(coffee)
coffee['lungo'] = '룽고'    #요소를 추가
print("요소추가:", coffee)

# (2) dict 변경 ==> 내부적으로 union으로 처리된다.
coffee['latte'] = '라떼2'
print("요소변경:",coffee)

# (3) dict 삭제 ==> del
del coffee['lungo']        #요소를 삭제
print("요소삭제1:",coffee)

coffee.pop('latte')        #요소를 삭제
print("요소삭제2:",coffee)

coffee.clear()            #요소 전체 삭제
print("요소전체삭제:",coffee) # { } 빈 값 출력

# (4) 병합 또는 한꺼번에 수정: update
x = {'name':'유관순','age':20}
y = {'address':'seoul'}
x.update(y)
print("병합1:",x) # {'name': '유관순', 'age': 20, 'address': 'seoul'}

x.update({'name':'aaa2','age':202}) # >> 기존 name, age의 value 값 수정 됨
print("한꺼번에 병합2:",x) # {'name': 'aaa2', 'age': 202, 'address': 'seoul'}

#  (5) dict  정보 얻기
coffee = {'espresso': '에스프레소', 'latte': '라떼'}
print(coffee)
print(len(coffee))  # 길이 출력, 2
print()

## key 값을 알고있는 경우
print(coffee['espresso'])  # 키를 이용해 값을 조회,  없으면 에러 , 에스프레소
print(coffee.get('latte'))  # key로 value 얻기 , 라떼
print(coffee.get('latt2e', 'Not a Coffee'))  #  없으면 기본값 출력 , 기본값 지정안하면 None 출력
print()

## key 값이 너무 많거나, 모르는 경우 사용
print(coffee.keys(), list(coffee.keys()))  # key 목록 출력, dict_keys(['espresso', 'latte'])
keys = list(coffee.keys())  # ['espresso', 'latte']
print(coffee[keys[0]], coffee['espresso'], coffee.get(keys[0])) # 에스프레소
print()

#value 값만 조회
print(coffee.values(), list(coffee.values()))  # value 목록 출력, dict_values(['에스프레소', '라떼'])
print()

##key value 값 조회
print(coffee.items(), list(coffee.values()))  # key, value 출력, dict_items([('espresso', '에스프레소'), ('latte', '라떼')])