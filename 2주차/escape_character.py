Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

================== RESTART: F:\파이썬예제코드_3반\1주차\exam1.py ==================
2523049
abc
def
>>> print("123" + "456")
123456
>>> print("ko"+"rea")
korea
>>> print(123+456)
579
>>> print("123+456","=",123+456)
123+456 = 579
>>> # escape character
>>> print
<built-in function print>
>>> print(""안녕"하고말했다")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("\"안녕\"하고 말했다")
"안녕"하고 말했다
>>> print("\'안녕\' 하고 말하는 듯 했다")
'안녕' 하고 말하는 듯 했다
>>> pint("\'안녕\'\n하고 말하는 듯 했다")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    pint("\'안녕\'\n하고 말하는 듯 했다")
NameError: name 'pint' is not defined. Did you mean: 'print'?
>>> print("\'안녕\'\n하고 말하는 듯 했다")
'안녕'
하고 말하는 듯 했다
>>> print("소망\t사랑\t믿음")
소망	사랑	믿음
>>> print("\\t여러칸 이동하는 이스케이프 문자 입니다.")
\t여러칸 이동하는 이스케이프 문자 입니다.
