#변수 만들기/사용하기
pi = 3.14159265
print(pi)
# 3.14159265
print(pi + 2)
print(pi - 2)
print(pi * 2)
print(pi / 2)
print(pi % 2)
print(pi * pi)
print()
# but 다른 타입의 변수랑 연산할 경우 에러

# 복합 대입 연산자 +=
number = 100
number += 10
number += 20
number += 30
print("number:", number)
# number: 160
print()

# 문자열 복합 대입 연산자
String = "안녕하세요"
String += "!"
String += "!"
print("String:", String)
# String: 안녕하세요!!
print()

#사용자 입력: input()
#input("인사말을 입력하세요> ")
string = input("인사말을 입력하세요> ")
print(string)
print()

#input() 함수의 입력 자료형
print(type(string))
print()

#문자열을 숫자로 바꾸기
string_a = input("입력 A> ")
int_a = int(string_a)

string_b = input("입력 B> ")
int_b = int(string_b)

print("문자열 자료:", string_a + string_b)
print("숫자 자료", int_a + int_b)
print()

#int()함수와 float()함수 활용
output_a = int("52")
output_b = float("52.273")

print(type(output_a), output_a)
print(type(output_b), output_b)
print()

#int()함수와 float()함수 조합
input_a = float(input("첫 번째 숫자> "))
input_b = float(input("두 번째 숫자> "))

print("덧셈 결과:", input_a + input_b)
print("뺄셈 결과:", input_a - input_b)
print("곱셈 결과:", input_a * input_b)
print("나눗셈 결과:", input_a / input_b)
print()

#str()함수를 사용해 숫자를 문자열로 변환
out_a = str(52)
out_b = str(52.273)
print(type(out_a), out_a)
print(type(out_b), out_b)
print()

# inch 단위를 cm 단위로 변경
# 숫자를 입력 받습니다.
raw_input = input("inch 단위의 숫자를 입력해주세요: ")

# 입력받은 데이터를 숫자 자료형으로 변경하고, cm 단위로 변경합니다
inch = int(raw_input)
cm = inch * 2.54

# 출력
print(inch, "inch는 cm 단위로", cm, "cm입니다.")