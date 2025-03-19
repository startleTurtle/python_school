# 다양한 형태의 부동 소수점 출력
output_a = "{:f}".format(52.273)
output_b = "{:15f}".format(52.273)
output_c = "{:+15f}".format(52.273)
output_d = "{:+015f}".format(52.273)

print(output_a)
print(output_b)
print(output_c)
print(output_d)
print()

# 소수점 아래 자릿수 지정
output_e = "{:15.3f}".format(52.273)
output_f = "{:15.2f}".format(52.273)
output_g = "{:15.1f}".format(52.273)

print(output_e)
print(output_f)
print(output_g)
print()

# 의미 없는 소수점 제거하기
output_h = 52.0
output_i = "{:g}".format(output_h)

print(output_h)
print(output_i)
print()

# upper(), lower()
# a = "Hello Python Programming..!"
# print(a.upper()) # 모두 대문자로
# print(a.lower()) # 모두 소문자로

# strip() 문자열 양옆의 공백 제거
input_a = """
    안녕하세요
문자열의 함수를 알아봅시다
"""
print(input_a.strip())
print()

# 문자열의 구성 파악 isoo()
print("TrainA10".isalnum())
print("10".isdigit())
print()

# 문자열 찾기 find(), rfind()
output_j = "안녕안녕하세요".find("안녕") # find(): 왼쪽부터 찾아서 처음 등장하는 위치를 찾음
print(output_j)

output_k = "안녕안녕하세요".rfind("안녕") # rfind(): 오른쪽부터 찾아서 처음 등장하는 위치를 찾음
print(output_k)
print()

# 문자열과 in 연산자
print("안녕" in "안녕하세요") # true
print("잘자" in "안녕하세요") # false
print()

# 문자열 자르기 split()
a = "10 20 30 40 50".split(" ")
print(a)
print()

# f-문자열
