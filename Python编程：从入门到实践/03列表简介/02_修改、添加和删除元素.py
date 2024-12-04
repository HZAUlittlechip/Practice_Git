#列表元素的替换吧和常规的变量替换应该是一样的

# 3.2.1 修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles[-1] = 'toyota'
print(motorcycles)

# 3.2.2 在列表中添加元素
# 增宽列表？然后插入？

# 01. 在列表末尾添加元素[append]
motorcycles.append('honda')
print(motorcycles) # ['ducati', 'yamaha', 'toyota', 'honda']
# 动态的分别插入变量
# 这种创建列表的⽅式极其常⻅，因为经常要等程序运⾏后，你才知道⽤户要在程序中存储哪些数据。
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
print(motorcycles) # ['honda', 'yamaha']

# 02. 在列表中插⼊元素[insert]
# 这种操作将列表中的每个既有元素都右移⼀个位置。
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)
motorcycles.insert(1,'mike')
print(motorcycles)

# 3.2.3 从列表中删除元素
# 01 [del ]
del motorcycles[1]
print(motorcycles)

# 02. 使⽤ pop() ⽅法删除元素
# pop() ⽅法删除列表末尾的元素，并让你能够接着使⽤它
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)  # ['honda', 'yamaha']
print(popped_motorcycles) # suziki 单一一个变量，被删除的变量被赋予给了pop

# 03. 删除列表中任意位置的元素
first_owned = motorcycles.pop(0)

# *** 如果不确定该使⽤ del 语句还是 pop() ⽅法，下⾯是⼀个简单的判断
# 标准：如果要从列表中删除⼀个元素，且不再以任何⽅式使⽤它，就
# 使⽤ del 语句；如果要在删除元素后继续使⽤它，就使⽤ pop() ⽅
# 法。 ***

# 04. 根据值删除元素
# remove()
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('honda')
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)  # remove函数中只能包含一个元素argument

# Q：如果我想知道某个元素在列表中的位置如何处理？
# Q：有根据元素名来返回元素位置的函数吗？[list.index()]
my_list = [10, 20, 30, 40, 50]
element = 30

# 获取元素在列表中的索引
index = my_list.index(element) #.index 返还的是第一个搜索到的元素

print(f"元素 {element} 在列表中的位置是：{index}")








