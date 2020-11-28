
# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banan']
print("Now ID is:", id(shoplist))

#对此 List （可变数据类型）重新赋值，地址发生改变
shoplist = ['apple', 'mango', 'carrot', 'banana']
print("Now ID is:", id(shoplist))

print('I have', len(shoplist), 'items to purchase.')

print('These items are:', end = ' ')
for item in shoplist:
    print(item, end = ' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

#修改（例如append、+=，与赋值 `=` 区分）此 List （可变数据类型），地址不变
print("Now ID is:", id(shoplist))

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)


""" Python列表函数&方法
Python包含以下函数:

序号	函数
1	len(list)
列表元素个数
2	max(list)
返回列表元素最大值
3	min(list)
返回列表元素最小值
4	list(seq)
将元组转换为列表
Python包含以下方法:

序号	方法
1	list.append(obj)
在列表末尾添加新的对象
2	list.count(obj)
统计某个元素在列表中出现的次数
3	list.extend(seq)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)
从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj)
将对象插入列表
6	list.pop([index=-1])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)
移除列表中某个值的第一个匹配项
8	list.reverse()
反向列表中元素
9	list.sort( key=None, reverse=False)
对原列表进行排序
10	list.clear()
清空列表
11	list.copy()
复制列表 """