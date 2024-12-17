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