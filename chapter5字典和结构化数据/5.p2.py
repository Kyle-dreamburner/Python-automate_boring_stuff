#-*-coding:utf-8-*-

#列表到字典的函数，针对好玩游戏物品清单
#好玩游戏的物品清单
#假设征服一条龙的战利品表示为这样的字符串列表：
#dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#写一个名为 addToInventory(inventory, addedItems)的函数， 其中 inventory 参数
#是一个字典， 表示玩家的物品清单（像前面项目一样）， addedItems 参数是一个列表，
#就像 dragonLoot。
#addToInventory()函数应该返回一个字典， 表示更新过的物品清单。请注意， 列
#表可以包含多个同样的项。

Inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby','fox']

def addToInventory(inventory, addedItems):
	for k in addedItems:
		inventory.setdefault(k, 0)
		i = 0
		i = i + 1
		inventory[k] = inventory[k] + i
	print (inventory)
	
addToInventory(Inventory, dragonLoot)