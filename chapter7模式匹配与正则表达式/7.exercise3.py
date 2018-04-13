#-*-coding:utf-8-*-
#22． 如何编写一个正则表达式匹配一个句子，它的第一个词是 Alice、 Bob 或
#Carol， 第二个词是 eats、 pets 或 throws， 第三个词是 apples、 cats 或 baseballs。该句
#子以句点结束。 这个正则表达式应该不区分大小写。它必须匹配：
# 'Alice eats apples.'
# 'Bob pets cats.'
# 'Carol throws baseballs.'
# 'Alice throws Apples.'
# 'BOB EATS CATS.'
#但不匹配：
# 'RoboCop eats apples.'
# 'ALICE THROWS FOOTBALLS.'
# 'Carol eats 7 cats.'

import re
name = ['Alice','Bob','Carol']
do = ['eats', 'pets', 'throws']
thing = ['apples', 'cats', 'baseballs']



sentenceRegex = re.compile(r'((Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.)', re.I)
mo = sentenceRegex.search('Carol throws baseballs.')
 
print (mo.group())