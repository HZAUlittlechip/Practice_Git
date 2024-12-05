# 5.3.1 简单的 if 语句

# 5.3.2 if-else 语句

# 5.3.3 if-elif-else 语句 检查两个以上的情形
# 它依次检查每个条件测试，直到遇到通过了的条件测试。
# 条件测试通过后，Python将执⾏紧跟在它后⾯的代码，并跳过余下的条件测试

# if-elif-else 语句虽然功能强⼤，但仅适⽤于只有⼀个条件满⾜的情
# 况：在遇到通过了的条件测试后，Python 就会跳过余下的条件测试。【缺点】
age = 18
if age < 18:
	print('free')
elif age == 18:   # 注意是elif
	print('yes')
else:
	print('no')  # yes

# 更加简介的code
if age < 18 or age >60:
	number = 'free'
elif age == 18:
	number = 'yes'
else:
	number = 'no'

print(f'you cost is {number}')
# else 是⼀条包罗万象的语句，只要不满⾜任何 if 或 elif 中的条件测
# 试，其中的代码就会执⾏。这可能引⼊⽆效甚⾄恶意的数据.

# else： 后面不需要加条件语句；
# elif ...: elif后面是需要添加条件语句的

# 5.3.6 测试多个条件
# 有时候必须检查你关⼼的所有条件。在这种情况下，应使⽤⼀系列
# 不包含 elif 和 else 代码块的简单 if 语句

# pizza 店的案例
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
 print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
 print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
 print("Adding extra cheese.")
 print("\nFinished making your pizza!")

