
# 列表是序列的一种表现形式
shoplist = ['apple', 'mango', 'carrot', 'banana']

# 字符串亦是序列的一种表现形式
name = 'swaroop'

# Indexing or 'Subscription' operation 
# 索引或“下标（Subscription）”操作符 
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# Slicing on a list 
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# 从某一字符串中切片 
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

# 第三个参数：步长
print(shoplist[::3])
print(shoplist[::-1])

# 以上的方法对元组、字符串、列表均有效
