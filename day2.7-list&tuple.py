# -*- coding: utf-8 -*-
print('数据类型list:是一种有序的合集')
print('classmates=[\'Michael\',\'Bob\',\'Tracy\']\n')
print('\n')

print('列出list')
print('classmates')
classmates=['Michael','Bob','Tracy']
print(classmates,'\n')
print('\n')

print('获得list元素的个数')
print('len(classmates)')
print(len(classmates),'\n')
print('\n')

print('用索引访问list中每一个位置的元素，索引从0开始')
print('classmates[0]')
print(classmates[0],'\n')
print('classmates[1]')
print(classmates[1],'\n')
print('classmates[2]')
print(classmates[2],'\n')
print('classmates[3]')
print('当索引超出范围，则报indexError错误')
print('IndexError: list index out of range')
print('最后一个元素的索引是len(classmates)-1')




print('\n')
print('\n')

print('''
如果要是取最后一个元素，可以倒数:
classmates[-1]
'Tracy'

classmates[-2]
'Bob'

classmates[-3]
'Michael'

classmates[-4]
ndexError: list index out of range(越界了)
''')


print('\n')
print('\n')

print('''
list是一个可变的有序表
\n
往list中追加元素到末尾
classmates.append('Adam')
''')
classmates.append('Adam')
print(classmates)

print('\n')
print('''
把元素插入到指定位置，比如索引号为[1]
classmates.insert(1,'Jack')
''')
classmates.insert(1,'Jack')
print(classmates)


print('\n')
print('''
删除list末尾元素，使用pop()方法
classmates.pop()
'Adam'
''')
classmates.pop()
print(classmates)


print('\n')
print('''
要删除指定位置的元素，用pop(i)方法，i是索引位置
classmates.pop(1)
'Jack'
''')
classmates.pop(1)
print(classmates)
print('\n')

