#-*-coding:utf-8-*-

#strip()的正则表达式版本
#写一个函数，它接受一个字符串， 做的事情和 strip()字符串方法一样。如果只
#传入了要去除的字符串， 没有其他参数， 那么就从该字符串首尾去除空白字符。否
#则， 函数第二个参数指定的字符将从该字符串中去除。

import re

string = input()
character = input()

def newstrip(str, char):
	strRegex = re.compile(r'(\s)(\w+)(\s)')
	mo = strRegex.search(str)
	if mo != None:
		print (''.join(mo.group(2).split(char)))
	else:
		print (str)
	
		
newstrip(string, character)
