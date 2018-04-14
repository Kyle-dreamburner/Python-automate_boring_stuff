#! python3
#-*-coding:utf-8-*-

#8.9.1 扩展多重剪贴板

#针对要检查的关键字，提供命令行参数。
#• 如果参数是 save，那么将剪贴板的内容保存到关键字。
#• 如果参数是 list，就将所有的关键字拷贝到剪贴板。
#• 否则，就将关键词对应的文本拷贝到剪贴板。
#扩展本章中的多重剪贴板程序，增加一个 delete <keyword>命令行参数，它将
#从 shelf 中删除一个关键字。然后添加一个 delete 命令行参数，它将删除所有关键字。

# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads corresponded content to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
	#List keywords and load content.
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()