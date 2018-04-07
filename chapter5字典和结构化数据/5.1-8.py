#-*-coding:utf-8-*-

#1. 空字典的代码是怎样的？
# {}

#2． 一个字典包含键'fow'和值 42， 看起来是怎样的？
#{'fow':42}

#3．字典和列表的主要区别是什么？
# 字典输入时用{},列表用[]。 字典中的索引可使用多种数据类型，不像列表，只能使用整数
# 进行索引。字典的索引被称为键，键及其关联的值，称为“键值对”。
# 字典中的表项值是不排序的，所以也不能像列表一样，使用切片。

#4．如果 spam 是{'bar': 100}， 你试图访问 spam['foo']， 会发生什么？
# 会发生KeyError:'foo'的错误

#5．如果一个字典保存在 spam 中， 表达式'cat' in spam 和'cat' in spam.keys()之间
#的区别是什么？
# 没有区别。都是表达‘cat’键在spam中.'in'操作符检查一个值是不是字典中的一个键。

#6． 如果一个字典保存在变量中， 表达式'cat' in spam 和'cat' in spam.values()之间
#的区别是什么？
# 'cat' in spam : 表达的是'cat' 键在spam中。检查字典中是不是有一个'cat'键。
# 'cat' in spam.values():表达的是值'cat'，在字典spam中。检查是否有一个值'cat'
# 对应spam中的某个键


#7． 下面代码的简洁写法是什么？
#if 'color' not in spam:
#spam['color'] = 'black'
# 简洁写法spam.setdefault('color','black')


#8． 什么模块和函数可以用于“漂亮打印”字典值？
# 使用模块'pprint',函数pprint(),pformat()
# 使用时，应是：
# import pprint：
# pprint.pprint(someDictionaryValue)
# print(pprint.pformat(someDictionaryValue))