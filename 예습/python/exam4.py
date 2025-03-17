# 문자열의 format()함수
# format()함수로 숫자를 문자열로 변환
string_a = "{}".format(10)

# 출력하기
print(string_a)
print(type(string_a))
print()

# format() 함수의 다양한 형태
# format() 함수로 숫자를 문자열로 변환
format_a = "{}만 원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)
print()

# format() 함수의 다양한 기능
# 정수를 특정 칸에 출력하기
# 정수
output_a = "{:d}".format(52)

# 특정 칸에 출력하기
output_b = "{:5d}".format(52)
output_c = "{:10}".format(52)

# 빈칸을 0으로 채우기
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

print("# 기본")
print(output_a)
print("# 특정 칸에 출력하기")
print(output_b)
print(output_c)
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)
print()

# 기호를 붙여 출력
output_f = "{:+d}".format(52)   # 양수
output_g = "{:+d}".format(-52)  # 음수
output_h = "{: d}".format(52)   # 양수: 기호 부분 공백
output_i = "{: d}".format(-52)  # 음수: 기호 부분 공백

print("# 기호와 함께 출력하기")
print(output_f)
print(output_g)
print(output_h)
print(output_i)
print()

#조합
output_j = "{:+5d}".format(52)      # 기호를 뒤로 밀기: 양수
output_k = "{:+5d}".format(-52)     # 기호를 뒤로 밀기: 음수
output_l = "{:=+5d}".format(52)     # 기호를 앞으로 밀기: 양수
output_m = "{:=+5d}".format(-52)    # 기호를 앞으로 밀기: 음수
output_n = "{:+05d}".format(52)     # 0으로 채우기: 양수
output_o = "{:+05d}".format(-52)    # 0으로 채우기: 음수

print("# 조합하기")
print(output_j)
print(output_k)
print(output_l)
print(output_m)
print(output_n)
print(output_o)

#