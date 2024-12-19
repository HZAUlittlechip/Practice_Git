def greet_user():
	"""显示简单的问候语"""
	print('Hello')

greet_user() # 定义的函数口号里是其需要的变量

# 8.1.1 向函数传递信息
def greet_user(user_name):
	""" 显示简单的问候语 """
	print(f'Hello,{user_name.title()}.')

greet_user('jeff')

# 8.1.2 实参和形参
