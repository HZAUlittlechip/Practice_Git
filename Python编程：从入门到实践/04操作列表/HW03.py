# 练习 4.1：⽐萨 想出⾄少三种你喜欢的⽐萨，将其名称存储在⼀个列
# 表中，再使⽤ for 循环将每种⽐萨的名称打印出来。
pizzas = ['first','second','third']
for pizza in pizzas:
   print(pizza)
# 修改这个 for 循环，使其打印包含⽐萨名称的句⼦，⽽不仅仅是
# ⽐萨的名称。对于每种⽐萨都显⽰⼀⾏输出，如下所⽰ I like pepperoni pizza;
   print(f"I like {pizza} pizza.")

# 练习 4.2 动物

# 练习 4.3：数到 20 使⽤⼀个 for 循环打印数 1〜20（含）
for value in range(1,21):
   print(value)

# 练习 4.4：100 万 创建⼀个包含数 1〜1 000 000 的列表，再使⽤⼀个
# for 循环将这些数打印出来。（如果输出的时间太⻓，按 Ctrl + C 停⽌
# 输出，或关闭输出窗⼝。）
list_numbers = list(range(1,1000001))
list_numbers = []
for number in range(1,1000001):
   list_numbers.append(number)
print(list_numbers)

for number in list_numbers:
   print(number)

# 练习 4.5：100 万求和 创建⼀个包含数 1〜1 000 000 的列表，再使⽤
# min() 和 max() 核实该列表确实是从 1 开始、到 1 000 000 结束的。
# 另外，对这个列表调⽤函数 sum()，看看 Python 将 100 万个数相加需
# 要多⻓时间。
print(max(list_numbers))
print(min(list_numbers))
print(sum(list_numbers))

# 练习 4.6：奇数 通过给 range() 函数指定第三个参数来创建⼀个列
# 表，其中包含 1〜20 的奇数；再使⽤⼀个 for 循环将这些数打印出
# 来。
single_numbers = range(1,21,2)
for single_number in single_numbers:
   print(single_number)

# 练习 4.7：3 的倍数 创建⼀个列表，其中包含 3〜30 内能被 3 整除的
# 数，再使⽤⼀个 for 循环将这个列表中的数打印出来。
three_numbers = range(3,31,3)
for three_number in three_numbers:
   print(three_number)

# 练习 4.8：⽴⽅ 将同⼀个数乘三次称为⽴⽅。例如，在 Python 中，2
# 的⽴⽅⽤ 2**3 表⽰。创建⼀个列表，其中包含前 10 个整数（1〜
# 10）的⽴⽅，再使⽤⼀个 for 循环将这些⽴⽅数打印出来。
lifang_numbers = []
for value in range(1,11):
   lifang_number = value**3
   lifang_numbers.append(lifang_number)
   print(lifang_number)

# 练习 4.9：⽴⽅推导式 使⽤列表推导式⽣成⼀个列表，其中包含前 10
# 个整数的⽴⽅。
lifang_numbers = list(value**3 for value in range(1,11))

# 练习 4.10：切⽚ 选择你在本章编写的⼀个程序，在末尾添加⼏⾏代
# 码，以完成如下任务。
test_list = lifang_numbers[:]

# 打印消息“The first three items in the list are:”，再使⽤切⽚来打印列
# 表的前三个元素。
print(f"The first three items in the list are: "
      f"{", ".join(map(str,test_list[0:3]))}") # map(str, )将整数类型的数列变为字符串的类型才能用join函数

# 打印消息“Three items from the middle of the list are:”，再使⽤切⽚
# 来打印列表中间的三个元素。
print(f"Three items from the middle of the list are: "
      f"{", ".join(map(str,test_list[3:6]))}")

# 打印消息“The last three items in the list are:”，再使⽤切⽚来打印列
# 表末尾的三个元素。
print(f"Three items from the middle of the list are: "
      f"{", ".join(map(str,test_list[-3:]))}")

# 练习 4.11：你的⽐萨，我的⽐萨 在你为练习 4.1 编写的程序中，创建
# ⽐萨列表的副本，并将其赋给变量 friend_pizzas，再完成如下任
# 务
friend_pizzas = pizzas[:]
print(friend_pizzas)

# 在原来的⽐萨列表中添加⼀种⽐萨
# 在列表 friend_pizzas 中添加另⼀种⽐萨。
pizzas.append('fourth')     # insert()函数也可以插入元素
friend_pizzas.append('4')

# 核实有两个不同的列表。为此，打印消息“My favorite pizzas
# are:”，再使⽤⼀个 for 循环来打印第⼀个列表；打印消息“My
# friend's favorite pizzas are:”，再使⽤⼀个 for 循环来打印第⼆个列
# 表。核实新增的⽐萨被添加到了正确的列表中。
print("my favorite pizzas are:")
for my_pizza in pizzas:
   print(my_pizza)

print("my friend favorite pizzas are:")
for friend_pizza in friend_pizzas:
   print(friend_pizza)

# 练习 4.12：使⽤多个循环 在本节中，为节省篇幅，程序 foods.py 的
# 每个版本都没有使⽤ for 循环来打印列表。请选择⼀个版本的
# foods.py，在其中编写两个 for 循环，将各个⾷品列表都打印出来。
  # ******* 有点无聊不打了 ************
