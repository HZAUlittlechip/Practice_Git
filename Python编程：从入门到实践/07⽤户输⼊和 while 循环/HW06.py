# 练习 7.1：汽⻋租赁 编写⼀个程序，询问⽤户要租什么样的汽⻋，并
# 打印⼀条消息，如下所⽰。
# Let me see if I can find you a Subaru.
car = input('Let me see if I can find you a')
print(car)

# 练习 7.2：餐馆订位 编写⼀个程序，询问⽤户有多少⼈⽤餐。如果超
# 过 8 个⼈，就打印⼀条消息，指出没有空桌；否则指出有空桌。
print('请问有多少人用餐:')

dinner_number = input()
dinner_number = int(dinner_number)  # int()函数也是临时改变函数
									# 需要对其重新赋予给变量
# 判断是否有空位置
if dinner_number <= 8:
	print('有空位置')
else:
	print('没有空位置')

# 练习 7.3：10 的整数倍 让⽤户输⼊⼀个数，并指出这个数是否是 10
# 的整数倍。
number = input('请输入一个数值，我来判断它是不是10的倍数：')
number = int(number)

if number % 10 == 0:
	print('它是10的整数倍')
else:
	print('它不是10的倍数')

# 练习 7.4：⽐萨配料 编写⼀个循环，提⽰⽤户输⼊⼀系列⽐萨配料，
# 并在⽤户输⼊ 'quit' 时结束循环。每当⽤户输⼊⼀种配料后，都打
# 印⼀条消息，指出要在⽐萨中添加这种配料。

prompt = ('请输入披萨的配料'
		  '\n输入‘quit’可以提出程序')

pizza = ''
active = True
while active:
	pizza = input(prompt)

	if pizza == 'quit':
		break
	else:
		print(pizza)

# 练习 7.5：电影票 有家电影院根据观众的年龄收取不同的票价：不到
# 3 岁的观众免费；3（含）〜12 岁的观众收费 10 美元；年满 12 岁的观
# 众收费 15 美元。请编写⼀个循环，在其中询问⽤户的年龄，并指出其
# 票价。

prompt = ('请输入你的年龄来看你的票价'
		  '\n你可以输入’退出‘退出程序')

age = ''
money = 0
while active:
	age = input(prompt)

	# 退出循环的情况
	if age == '退出':
		break
	else:
		age = int (age)   #在 age 不是退出的时候 将其转化为整型

	if age < 3:
		money = 0
		print(f'你是免费的')
	else:
		if age < 12:
			money = 10
		else:
			money = 15
		print(f"你的票价是{money}美元")

# 练习 7.7：⽆限循环 编写⼀个没完没了的循环，并运⾏它。（要结束
# 该循环，可按 Ctrl + C，也可关闭显⽰输出的窗⼝。）
# x = 1
# while x <= 5:
# 	print(x)

# 练习 7.8：熟⾷店 创建⼀个名为 sandwich_orders 的列表，其中
# 包含各种三明治的名字，再创建⼀个名为 finished_sandwiches
# 的空列表。遍历列表 sandwich_orders，对于其中的每种三明治，
# 都打印⼀条消息，如“I made your tuna sandwich.”，并将其移到列表
# finished_sandwiches 中。当所有三明治都制作好后，打印⼀条消
# 息，将这些三明治列出来。

sandwich_orders = ['one','two','three']
finished_sandwiches = []

while sandwich_orders:
	finished_sandwiche = sandwich_orders.pop()
	finished_sandwiches.append(finished_sandwiche)

# 所有三明治 做好后在输出
print('做好的三明治有：', end='')
for finished_sandwiche in finished_sandwiches:
	print(finished_sandwiche, end=" ")

# 练习 7.9：五⾹烟熏⽜⾁卖完了 使⽤为练习 7.8 创建的列表
# sandwich_orders，并确保 'pastrami' 在其中⾄少出现了三次。
# 在程序开头附近添加这样的代码：先打印⼀条消息，指出熟⾷店的五
# ⾹烟熏⽜⾁（pastrami）卖完了；再使⽤⼀个 while 循环将列表
# sandwich_orders 中的 'pastrami' 都删除。确认最终的列表
# finished_sandwiches 中未包含 'pastrami'。
sandwich_orders = ['one','two','three','pastrami','pastrami','pastrami']

print('不好意思，五香牛肉卖完啦！')

beef_active = True
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

print(sandwich_orders)

# 练习 7.10：梦想中的度假胜地 编写⼀个程序，调查⽤户梦想中的度
# 假胜地。使⽤类似于“If you could visit one place in the world, where
# would you go?”的提⽰，并编写⼀个打印调查结果的代码块。
prompt = ('f you could visit one place in the world, where '
		  'would you go:\n do not want to again say no')

active = True
while active:
	place = input(prompt)
	if place == 'no':
		active = False
		print('Thank for your attending')
	else:
		print(f'{place} is a nice place')

# 7.4 ⼩结
# 在本章中，你⾸先学习了如何在程序中使⽤ input() 来让⽤户提供信息，
# 如何处理⽂本和数的输⼊，以及如何使⽤ while 循环让程序按⽤户的要求
# 不断地运⾏。然后⻅识了多种控制 while 循环流程的⽅式：设置活动标
# 志，使⽤ break 语句，以及使⽤ continue 语句。你还学习了如何使⽤
# while 循环在列表之间移动元素，以及如何从列表中删除所有包含特定值
# 的元素。最后，你学习了如何结合使⽤ while 循环和字典。
