'''
     JSON 변환

       1. json --> 문자열
         import json

         json.dumps(json)

       2.  문자열 -->  json

          json.loads(문자열)
'''

import json

#1. 문자열 --> json
s = '{"username":"홍길동", "age":20}'
print(s,type(s)) # <class 'str'>

s_json = json.loads(s)
print(s_json,type(s_json)) # <class 'dict'>
print(s_json["username"], s_json["age"])

l_s = "[10,20,30]"
print(l_s,type(l_s)) # <class 'str'>

ls_json = json.loads(l_s)
print(ls_json,type(ls_json)) # <class 'list'>
print(ls_json[0], ls_json[1], ls_json[2])

print("#"*100)

#2. json --> 문자열
s_json = {"username":"홍길동", "age":20}
print(s_json,type(s_json)) # <class 'dict'>
s = json.dumps(s_json)
print(s,type(s)) # <class 'str'>
