# False로 처리되는 데이터
print(not 0)
print(not None)
print(not "")
print(not [])
print(not {}) # 비어있는 dict
print(not set()) #비어있는 set

# True로 처리되는 데이터
print(not 10)
print(not "aa")
print(not [1,2])
print(not {"age" : 20})
