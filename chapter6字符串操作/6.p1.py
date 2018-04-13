#-*-coding:utf-8-*-
#编写一个名为 printTable()的函数， 它接受字符串的列表的列表，将它显示在组
#织良好的表格中， 每列右对齐。假定所有内层列表都包含同样数目的字符串。例如，
#该值可能看起来像这样：
#tableData = [['apples', 'oranges', 'cherries', 'banana'],
#['Alice', 'Bob', 'Carol', 'David'],
#['dogs', 'cats', 'moose', 'goose']]
#你的 printTable()函数将打印出：
#  apples  Alice  dogs
# oranges    Bob  cats
#cherries  Carol moose
#  banana  David goose


tableData = [['apples', 'oranges', 'cherries', 'banana','pear'],
['Alice', 'Bob', 'Carol', 'David', 'Kyle'],
['dogs', 'cats', 'moose', 'goose', 'pig']]

def printTable(rawData):
	colWidths = [0] * len(rawData)
	for i in range(len(rawData)):
		colWidths[i] = len(max(rawData[i], key = len))
	
	for k in range(len((rawData)[0])):
		for i in range(len(rawData)):
			print((rawData[i][k]).rjust(colWidths[i]) + str('  '), end = '')
		print('')
			
		
					
printTable(tableData)
			
