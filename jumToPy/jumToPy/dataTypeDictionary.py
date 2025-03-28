# 딕셔너리 기본형태
dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

# 딕셔너리 쌍추가
a = {1: 'a'}
a[2] = 'b'
a # {1: 'a', 2: 'b'}

a['name'] = 'pey'
a # {1: 'a', 2: 'b', 'name': 'pey'}

a[3] = [1, 2, 3]
a # {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

# 딕셔너리 요소 삭제
del a[1]
a # {2: 'b', 'name': 'pey', 3: [1, 2, 3]}

# 딕셔너리를 사용하는 방법
{"김연아": "피겨스케이팅", "류현진": "야구", "손흥민": "축구", "귀도": "파이썬"}

# 딕셔너리에서 key를 사용해 value 얻기
grade = {'pey': 10, 'julliet': 99}
grade['pey'] # 10
grade['julliet'] # 99

# 딕셔너리 관련 함수

# key 리스트 만들기 keys
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
a.keys() # dict_keys(['name', 'phone'm 'birth'])

# value 리스트 만들기 values
a.values() # dict_values(['pey', '010-9999-1234', '1118'])

# key, value 쌍 얻기 items
a.items() #dict_items([('name', 'pey'), ('phone', '010-9999-1234'), ('birth', '1118')])

# key:value 쌍 모두 지우기 clear
a.clear # {}

# key로 value 얻기 get
a.get('name') # 'pey'
a.get('phone') # '010-9999-1234'

# 딕셔너리 안에 key가 없을 경우
a.get('nokey', 'foo') # foo

# 해당 key가 딕셔너리 안에 있는지 조사하기 in
'name' in a # True
'email' in a # False