#-*-coding:utf-8-*-

#21． 如何写一个正则表达式， 匹配姓 Nakamoto 的完整姓名？ 你可以假定名字
#总是出现在姓前面， 是一个大写字母开头的单词。该正则表达式必须匹配：
# 'Satoshi Nakamoto'
# 'Alice Nakamoto'
# 'RoboCop Nakamoto'
#但不匹配：
# 'satoshi Nakamoto'（名字没有大写首字母）
# 'Mr. Nakamoto'（前面的单词包含非字母字符）
# 'Nakamoto' （没有名字）
# 'Satoshi nakamoto'（姓没有首字母大写）

import re
 
nameRegex = re.compile(r'([A-Z]\w+\s[A-Z]\w+)')
mo = nameRegex.search('Satoshi nakamoto')
 
print (mo.group())