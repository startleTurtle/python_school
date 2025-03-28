# 함수
def add(a, b):
    return a + b
print(add(3, 4))

# 입력 값이 없는 함수
def say():
    return 'Hi'
print(say())

# return 값이 없는 함수
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a + b))
add(3, 4)

# 입력값도 리턴 값도 없는 함수
def say():
    print('Hi')
say()

# 매개변수를 지정하여 호출
def sub(a, b):
    return a - b
result = sub(a = 7, b = 3)
print(result)

# 여러 개의 입력 값을 받는 함수
def add_many(*args):
    result = 0
    for i in args:
        result = result + i # *args에 입력받은 모든 값을 더한다.
    return result
result = add_many(1, 2, 3)
print(result)

result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

def add_mul(choice, * args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * 1
    return result
result = add_mul('add', 1, 2, 3, 4, 5)
print(result)
result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)

# 키워드 매개변수 kwargs
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a = 1)
print_kwargs(name = 'foo', age = 3)

# 함수의 리턴값은 언제나 하나
def add_and_mul(a, b):
    return a+b, a*b
result1, result2 = add_and_mul(3, 4)

def add_and_mul(a, b):
    return a + b
    return a * b
result = add_and_mul(2, 3)
print(result)

# return의 또 다른 쓰임새
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다." % nick)
say_nick('야호')
say_nick('바보')

# 매개변수에 초깃 값 미리 설정
def say_myself(name, age, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("박응용", 27)
say_myself("박응용", 27, True)
say_myself("박응용", 27, False)

# error
# def say_myself(name, man=True, age):
#     print("나의 이름은 %s 입니다." % name)
#     print("나이는 %d살입니다." % age)
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")

a = 1
def vartest(a):
    a = a + 1
vartest(a)
print(a)

def vartest(hello):
    hello = hello + 1
    
def vartest(a):
    a = a + 1

vartest(3)
print(a)

# return 사용
a = 1
def vartest(a):
    a = a + 1
    return
a = vartest(a)
print(a)

# global 명령어 사용
a = 1
def vartest():
    global a
    a = a + 1
    
vartest()
print(a)

# lambda 예약어
add = lambda a, b: a + b
result = add(3, 4)
print(result)

def add(a, b):
    return a + b
result = add(3, 4)
print(result)