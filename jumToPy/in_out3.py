# f = open("새파일.txt", 'w')
# f.close

# 파일_객체 = open(파일_이름, 파일_열기_모드)

'''
파일 열기모드
r: 일기 모드: 파일을 읽기만 할 때 사용
w: 쓰기 모드: 파일에내용을 쓸 때 사용
a: 추가 모드: 파일의 마지막에 새로운 내용을 추가할 때 사용
'''

# f = open("C:\Document\예습\python\jumToPy/새파일.txt", 'w')
# f.close

# f = open("C:\Document\예습\python\jumToPy/새파일.txt", 'w', encoding="utf-8")
# for i in range(1, 11):
#     data = "%d번째 줄입니다. \n" % i
#     f.write(data)
# f.close 

# f = open("C:/Document/예습/python/jumToPy/새파일.txt", 'r', encoding="utf-8")
# line = f.readline()
# print(line)
# f.close

# f = open("C:/Document/예습/python/jumToPy/새파일.txt", 'r', encoding="utf-8")
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

# f = open("C:/Document/예습/python/jumToPy/새파일.txt", 'r', encoding="utf-8")
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

# f = open("C:/Document/예습/python/jumToPy/새파일.txt", 'r', encoding="utf-8")
# lines = f.readlines()
# for line in lines:
#     line = line.strip() # 줄 끝의 줄 바꿈 문자를 제거
#     print(line)
# f.close

# f = open("C:/Document/예습/python/jumToPy/새파일.txt", 'r', encoding="utf-8")
# data = f.read()
# print(data)
# f.close()

# f = open("C:/Document/예습/python/jumToPy/새파일.txt", 'r', encoding="utf-8")
# for line in f:
#     print(line)
# f.close()

# f = open("C:/Document/예습/python/jumToPy/새파일.txt", 'a', encoding="utf-8")
# for i in range(11, 20):
#     data = "%d번째 줄입니다. \n" % i
#     f.write(data)
# f.close

f = open("C:/Document/예습/python/jumToPy/foo.txt", 'w', encoding="utf-8")
f.write("Life is too short, you need python")
f.close()
with open("C:/Document/예습/python/jumToPy/foo.txt", 'w') as f:
    f.write("Life is too short, you need python")