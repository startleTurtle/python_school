# money = True
# if money:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")
    
# 비교 연산자
# x < y: x가 y보다 작다.
# x > y: x가 y보다 크다.
# x == y: x와 y가 같다.
# x != y: x와 y가 같지 않다.
# x >= y: x가 y보다 크거나 같다.
# x <= y: x가 y보다 작거나 같다.

# money = 2000
# if money >= 3000:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")
    
# and, or not
# x or y: x와 y 둘 중 하나만 참이어도 참이다.
# x and y: x와 y 모두 참이어야 참이다.
# not x: x가 거짓이면 참이다

# money = 2000
# card = True
# if money >= 3000 or card:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")

# in, not in
# x in 리스트, x in 튜플, x in 문자열
# x not in 리스트, x not in 튜플, x not in 문자열

1 in [1, 2, 3] # True
1 not in [1, 2, 3] # False

'a' in ('a', 'b', 'c') # True
'j' not in 'python' # True

# 만약 주머니에 돈이 있으면 택시를 타고 가고, 없으면 걸어가라.
# pocket = ['paper', 'cellphone', 'money']
# if 'money' in pocket:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")

# pass 가끔 조건문의 참, 거짓에 따라 실행할 행동을 정의할 때나 아무런 일도 하지 않도록 설정하고 싶을 때
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
    
# elif
# 주머니에 돈이 있으면 택시, 주머니에 돈은 없지만 카드가 있으면 택시, 돈도 없고 카드도 없으면 걸어가라
'''
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고가라")
    else:
        print("걸어가라") '''
# 위 코드를 아래와 같이 수정 가능
'''
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")'''
# if문 한 줄로 작성
'''
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")'''
# 위 코드를 아래처럼
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")

# 조건부 표현식
score = 100
'''
if score >= 60:
    message = "success"
else:
    message = "failure" '''
# 간단하게
message = "success" if score >= 60 else "failure"