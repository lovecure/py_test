# -*- coding: utf-8 -*-

print('''
# 简单计算整数相加)
print(1+2+3)
''')

print(1+2+3)

print('\n')

print('''
# for 循环就是把每个元素带入变量，然后执行缩进块的语句

names = ['Michael','Bob','Tracy']
for name in names:
	print(name)
''')

name = ('zxx','wyx','zyq')
for family in name:
	print(family)

print('\n')

print('''
# Python提供了一个range()函数，可以生成一个整数序列，可以结合list()函数转换为list
\n
#生成序列是从0开始小于5的整数
list(range(5))
[0,1,2,3,4]
\n
#计算1-100所有整数之和
sum = 0
for x in range(101):
	sum = sum + x
print(sum)
''')
sum = 0
for x in range(101):
	sum = sum + x
print(sum)
