# for循环 和 while循环 的区别
from pyexpat.errors import messages

# 7.2.1 使⽤ while 循环

# 输出从1到5
current_number = 1
while current_number <= 5:  # 变量大于5时候跳出循环
	print(current_number)
	current_number += 1  # 变量自加1

for i in range(1,6):
	print(i)

# 7.2.2 让⽤户选择何时退出

# 让用户输入要求，并可以让其控制其退出
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ''
while message != 'quit':
	message = input(prompt)
	if message == 'quit':
		print(f'You have been quit the program')
	else:
		print(message)

# 7.2.3 使⽤标志 (flag)
# 在要求满⾜很多条件才继续运⾏的程序中，可定义⼀个变量，⽤于判断整
# 个程序是否处于活动状态。这个变量称为标志（flag)

# 定义一个函数指示灯来判定函数是否还在进行
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
	message = input(prompt)

# 标志 active 的测试 （全部都放在一起便于代码的阅读）
	if message == 'quit':
		active = False
		print(f'You have been quit the program')
	else:
		print(message)

# 7.2.4 使⽤ break 退出循环

# 7.2.5 在循环中使⽤ continue
# 返回循环开头，并根据条件测试的结果决定 *是否继续执⾏循环

current_number = -1

# 只输出奇数 --- 跳过偶数
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	else:
		print(current_number)

# 7.2.6 避免⽆限循环
# ctrl + c or 直接关闭程序的终端 Terminal