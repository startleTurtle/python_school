#숫자 종류
print(type(273))    #int
print(type(52.275)) #float
print()

#숫자 연산자 +, -, *, /
print("5 + 7 =", 5 + 7)
print("5 - 7 =", 5 - 7)
print("5 * 7 =", 5 * 7)
print("5 / 7 =", 5 / 7)
print()

#정수 나누기 연산자 //
print("3 / 2 =", 3 / 2)
print("3 // 2 =", 3 // 2)
print()

#나머지 연산자 %
print("5 % 2 =", 5 % 2)
print()

#제곱 연산자 **
print("2 ** 1 =", 2 ** 1)
print("2 ** 2 =", 2 ** 2)
print("2 ** 3 =", 2 ** 3)
print("2 ** 4 =", 2 ** 4)
print()

#연산자 우선순위 () >> *, / >> +, -
print(2 + 2 - 2 * 2 / 2 * 2)
print(2 - 2 + 2 / 2 * 2 + 2)
print()

#TypeEroor 예외
# String = "문자열"
# number = 273
# string + number = error

#문자열 우선순위
print("안녕" + "하세요" * 3)
# 안녕하세요하세요하세요
print(("안녕" + "하세요") * 3)
#안녕하세요안녕하세요안녕하세요
print("안녕" + ("하세요" * 3))
#안녕하세요하세요하세요
