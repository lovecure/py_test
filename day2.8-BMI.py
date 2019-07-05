# -*- coding: utf-8 -*-

height = 1.75
weight = 80.5
bmi = 80.5/(1.75*1.75)
if bmi<18.5:
	print('小明你的体重是',bmi)
	print('你的体重过轻')
elif bmi>=18.5 and bmi<=25:
	print('小明你的体重是',bmi)
	print('你的体重正常')
elif bmi>=25 and bmi<=28:
	print('小明你的体重是',bmi)
	print('你的体重过重')
elif bmi>=28 and bmi<=32:
	print('小明你的体重是',bmi)
	print('你的体重肥胖')
elif bmi>32:
	print('小明你的体重是',bmi)	
	print('你的体重严重肥胖')
