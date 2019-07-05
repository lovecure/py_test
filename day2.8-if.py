#!/data/data/io.neoterm/files/usr/bin/python3.6
# -*- coding: utf-8 -*-
print('例1:if语句判断是Ture则执行缩进的两行"print"')
print('''
age = 20
if age >= 18:
    print('your age is',age)
    print('adult')
''')
print('结果:')
age = 20
if age >= 18:
    print('your age is',age)
print('adult')

print('\n')
print('\n')






print('例2:如果if判断为False，不要执行if的内容，去执行else里的语句')
print('''age = 3
if age >= 18:
    print('your age is',age)
    print('adult')
else:
    print('your age is',age)
    print('teenager')
''')
print('结果:')
if age >= 18:
    print('your age is',age)
    print('adult')
else:
    print('your age is',age)
    print('teenager')

print('\n')
print('\n')





print('例3:可以使用elif做更精细的判断')
print('''age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kids')
''')
print('结果:')
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kids')

print('\n')
print('\n')


print('例:4if语句的特点是:它是从上往下判断，如果在某个判断上是Ture,把该判断对应的语句执行后，就忽略剩下的elif和else')
print('''
请判断下面的程序为什么打印的是teenager？
age = 20
if age >=6:
	print('teenager')
elif age >=18:
	print('adult')
else:
	print('kid')
''')
print('结果:')
age = 20
if age >=6:
    print('teenager')
elif age >=18:
    print('adult')
else:
    print('kid')
print('答:因为第一个条件已经是True，20>6所以if忽略之后的语句')

print('\n')
print('\n')
print('\n')

print('''例5:简写的if判断语句
if x:
	print('True')
''')
print('结果:')
x = 'x'
if x:
	print('True')

print('\n')
print('\n')
print('\n')

print('''
例6:input类型问题
birth = input('birth:')
if birth < 2000:
	print('00前')
else:
	print('00后')
输入任意年份，结果报错:"TypeError: unorderable types: str() > int()"
\n
这是因为input()返回的数据类型是"str","str"不能直接和整数比较，必须现把"str"转换成整数，Python提供了"int()"函数来完成这件事
''')

print('\n')

print('''
经过改良的程序:
s = input('birth:')
birth = int(s)
if birth < 2000:
	print('00前')
else:
	print('00后')
''')

print('结果:')
s = input('birth:')
birth = int(s)
if birth < 2000:
	print('00前')
else:
	print('00后')

print ('\n')
print ('''
可以得出正确的结果，但是如果输入abc，又会得出错误信息
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'abc'
\n
因为int()函数发现一个字符并不是合法的数字就会报错
''')
