food = "Python's favorite food is perl"

say = '"Python is very easy." he says.'

# food = 'Python's favorite food is perl' >> 에러
# \를 이용해 ', " 문자열에 추가하기
food = 'Python\'s favorite food is perl'
say = "\"Pythons is very easy.\" he says."

# 줄을 바꾸기 위한 이스케이프 코드 \n 삽입
multiline = "Life is too short\nYou need python"

# 연속된 작은 따옴표 3개 또는 큰 따옴표 3개 사용

# 연속된 작은 따옴표 3개
multiline = '''
Life is too short
You need Python
'''

# 연속된 큰 따옴표 3개
multiline = """
Life is too short
You need python
"""

# 이스케이프 코드
# \n : 줄바꿈
# \t : 문자열 사이 탭 간격
# \\ : \를 그대로 사용
# \' : 작은 따옴표(')를 그대로 표현할 때 사용
# \" : 큰 따옴표(")를 그대로 표현할 때 사용
# \r : 캐리지 리턴(줄 바꿈 문자, 커서를 현재 줄의 가장 앞으로 이동)
# \f : 폼 피드(줄 바꿈 문자, 커서를 현재 줄의 다음 줄로 이동)
# \a : 벨 소리(출력할 때 pc 스피커에서 '삑' 소리가 남)
# \b : 백 스페이스
# \000 : 널 문자

# 문자열 연산
head = "Python"
tail = " is fun!"

# 문자열 곱하기
a = "python"
a * 2

# 문자열 곱하기 응용
print("=" * 50)
print("My Program")
print("=" * 50)
print()

# 문자열 길이 구하기
a = "Life is too short"
len(a)

# 문자열 인덱싱
a = "Life is too short, You need Python"

# 문자열 슬라이싱
b = a[0] + a[1] + a[2] + a[3]
# >> Life

b = a[0:4] # >> Life

# 시작과 끝을 생략해도 됨
a[19:]
a[:17]

# 둘 다 생략시 시작 번호부터 끝 번호까지 뽑아냄
a[:]

# 슬라이싱 문자열 나누기 자주 사용하는 기법
a = "20230331Rainy"
date = a[:8]
weather = a[8:]

# Pithon 문자열을 Python으로 바꾸려면
a = "Piton"
a[:1] # P
a[2:] #thon
a[:1] + 'y' + a[:2]

# 문자열 포매팅
"I eat %d apples." % 3 # 숫자 대입
"I eat %s apples." % "five" # 문자열 대입

# 2개 이상의 값 넣기
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)

# 문자열 포맷 코드
# %s > 문자열
# %c > 문자
# %d > 정수
# %f > 부동소수(실수)
# %o > 8진수
# %x > 16진수
# %% > Literal %(문자 % 자체)

print("Error is %d%%." % 98)
print()

# 정렬과 공백
print("%10s" % "hi")
print("%-10sjane." % "hi")
print()

# 소수점 표현
print("%0.4f" % 3.42134234)
print()

# format 함수를 사용한 포매팅
print("I eat {0} apples".format(3))

# 문자열 발로 대입
print("I eat {0} apples".format("five"))

# 숫자 값을 가진 변수로 대입
number = 3
"I eat {0} apples".format(number)

# 2개 이상의 값 넣기
number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)

# 이름으로 넣기
"I ate {number} apples. so I was sick for {day} days.".format(number = 10, day = 3)

# 인덱스와 이름을 혼용해서 넣기
"I ate {0} apples. so I was sick for {day} days.".format(10, day = 3)

# 왼쪽 정렬
"{0:<10}".format("hi")
# 오른쪽 정렬
"{0:>10}".format("hi")
# 가운데 정렬
"{0:^10}".format("hi")

# 공백 채우기
"{0:=^10}".format("hi")  # ====hi====
"{0:!^10}".format("hi")  # hi!!!!!!!!

# 소수점 표현
y = 3.42134234
"{0:0.4f}".format(y) # 3.4213

# 문자 표현
"{{ and }}".format()  # '{ and }'

# f 문자열 포매팅
name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'

f'나는 내년이면 {age + 1}살이 된다.'

d = {'name':'홍길동', 'age':30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'

# f문자열 정렬
f'{"hi":<10}'  # 왼쪽 정렬
f'{"hi":>10}'  # 오른쪽 정렬
f'{"hi":^10}'  # 가운데 정렬

# f문자열 공백 채우기
f'{"hi":=^10}'  # 가운데 정렬하고 '=' 문자로 공백 채우기
f'{"hi":!<10}'  # 왼쪽 정렬하고 '!' 문자로 공백 채우기

# 소수점
y = 3.42134234
f'{y:0.4f}'  # 소수점 4자리까지만 표현
f'{y:10.4f}'  # 소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤

# f문자열에서 {}를 문자 그대로 표시하려면
f'{{ and }}'

# f문자열을 사용하여 금액에 , 사용
f"난 {1500000:,}원이 필요해" # 난 1,500,000원이 필요해

# 문자열 관련 함수

# count 문자 개수 세기
a = "hobby"
a.count('b') # 2

# find 위치 알려주기
a = "Python is the best choice"
a.find('b') # 14
a.find('k') # 존재하지 않으면 -1출력

# index 위치 알려주기 2
a = "Life is too short"
a.index('t') # 8
a.index('k') # 에러

# 문자열 삽입 join
",".join('abcd') # 'a,b,c,d'
",".join(['a', 'b', 'c', 'd']) # a,b,c,d

# 소문자를 대문자로 바꾸기 upper
a = "hi"
a.upper() #"HI"
# 대문자를 소문자로 바꾸기 lowrer
a = "HI"
a.lower # hi

# 왼쪽 공백 지우기 lstrip
a = " hi "
a.lstrip() # 'hi '
# 오른쪽 공백 지우기 rstrip
a.rstrip() # ' hi'
# 양쪽 공백 지우기 strip
a.strip() # 'hi'

# 문자열 바꾸기 replace
a = "Life is too short"
a.replace("Life", "Your leg")  # Your leg is too short

# 문자열 나누기 split
a.split() # ['Life', 'is', 'too', 'short']
b = "a:b:c:d"
b.split(':') #['a', 'b', 'c', 'd'] 