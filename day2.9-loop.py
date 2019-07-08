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

print('''
# while 循环:只要条件满足,就不断循环，条件不满足时退出循环

比如:计算100以内所有奇数之和，可以用while循环实现

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
    print(sum)


解释:
sum初始为0，n初始为99，99大于0，遂执行sum+99(0+99),再执行n-2(99-2=97)，再执行打印sum(99)

此时:
sum = 99
n = 97

执行下一个循环(因n>0)
sum = 99 + 97 = 196
n = 97 -2 = 95

再次打印sum(196)

执行下一个循环(因n>0)
sum = 196 + 95
n = 95 -2 

......
直到n < 0(-1),循环结束



''')

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
    print(sum)

print('\n')

print('''
#利用循环依次对list中的每个名字打印出Hello,xxx!

L = ['Bart','Lisa','Adam']

for l in L:
    print('Hello,',l,'!')

''')

L = ['Bart','Lisa','Adam']

for l in L:
    print('Hello,',l,'!')
