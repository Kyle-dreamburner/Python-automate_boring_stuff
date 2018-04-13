#-*-coding:utf-8-*-
#写一个函数，它使用正则表达式， 确保传入的口令字符串是强口令。 强口令的
#定义是： 长度不少于 8 个字符， 同时包含大写和小写字符， 至少有一位数字。你可
#能需要用多个正则表达式来测试该字符串， 以保证它的强度。

import re

print ('Please enter your code')
code = input()
if len(code) > 7:
	codeRegex = re.compile(r'''
	[A-Z]+[a-z]+[0-9]+|
	[A-Z]+[0-9]+[a-z]+|
	[a-z]+[A-Z]+[0-9]+|
	[a-z]+[0-9]+[A-Z]+|
	[0-9]+[a-z]+[A-Z]+|
	[0-9]+[A-Z]+[a-z]+
	
	''', re.VERBOSE)
	mo = codeRegex.search(code)
	if mo != None:
		print ('Pass')
	else:
		print('Please retry')
	
else:
	print ('your code should has more than 8 character')