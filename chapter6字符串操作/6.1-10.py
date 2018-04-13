#-*-coding:utf-8-*-

#1.什么是转义字符？
# "转义字符" 让你输入一些字符，它们用其他方式是不可能放在
# 字符串里面的。转义字符包含一个倒斜杠（\），紧跟着是需要添加
# 到字符串里面的符号

#2.转义字符\n 和\t 代表什么？
# '\n'代表换行；'\t'代表添加制表符

#3.如何在字符串中放入一个倒斜杠字符\？
# \\ 转义字符表示一个反斜杠

#4.字符串"Howl's Moving Castle"是有效字符串。为什么单词中的单引号没有转
#义， 却没有问题？
# 因为字符串以双引号开始，所以Python知道单引号是字符串的一部分，而不是表示字符串的结束。

#5.如果你不希望在字符串中加入\n， 怎样写一个带有换行的字符串？
# 使用3个单引号或3个双引号作为字符串的起止。“三重引号”之间的所有引号、制表符或换行，
# 都被认为是字符串的一部分

#6.下面的表达式求值为什么？
#'Hello world!'[1] => e
#'Hello world!'[0:5] => 'Hello '
#'Hello world!'[:5] => 'Hello '
#'Hello world!'[3:] => 'lo world!'

#7.下面的表达式求值为什么？
# 'Hello'.upper() => 'HELLO'
# 'Hello'.upper().isupper() => True
# 'Hello'.upper().lower() => 'hello'

#8.下面的表达式求值为什么？
#'Remember, remember, the fifth of November.'.split()
# ['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']

#'-'.join('There can be only one.'.split())
# 'There-can-be-only-one.'

#9.什么字符串方法能用于字符串右对齐、 左对齐和居中？
# 'Hello'.rjust(); 'Hello'.ljust(); 'Hello'.center()
# rjust(agv1:"20":总长度，agv2:"-": 代替空格的符号 )

#10.如何去掉字符串开始或末尾的空白字符？
# strip()字符串方法将返回一个新的字符串，他的开头和末尾没有空白字符串。
#lstrip(), rstrip()分别删除左边或右边的空白字符