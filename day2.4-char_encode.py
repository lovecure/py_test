# -*- coding: utf-8 -*-
print('包含中文的str')
print(ord('A'))
ord('中')
chr(66)
chr(25991)
'\u4e2d\u6587'
'ABC'.encode('ascii')
'中文'.encode('utf-8')
#'中文'.encode('ascii')
b'ABC'.decode('ascii')
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore')
len('ABC')
len('中文')
len(b'ABC')
len(b'\xe4\xb8\xad\xe6\x96\x87')
len('中文'.encode('utf-8'))
# -*- coding: utf-8 -*-