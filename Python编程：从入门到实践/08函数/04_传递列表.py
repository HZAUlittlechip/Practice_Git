# 定义函数来名字列表，循环的输出 列表中的名字
def greet_user(names):
	"""输入列表来循环祝福名字 """
	for name in names:
		print(f'Hello, {name}')

user_names = ['hannah', 'ty', 'margot']
greet_user(user_names)

# 8.4.1 在函数中修改列表

# 将需要打印的列表的变量转换到 已打印的列表中

def print_models(unprinted_designs,completed_models):
	""" 转移两个变量的列表 """
	while unprinted_designs:
		print_model = unprinted_designs.pop()
		print(f'{print_model}已经被打印')
		completed_models.append(print_model)

def show_model(completed_models):
	""" 显示所有打印好的模型 """
	print('\n下面的模型被打印出来了：')
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_model(completed_models)

# 8.4.2 禁⽌函数修改列表

# 创建 副本来保护不想修改的列表 ！
# 可讲 副本 传递给函数
# function_name(list_name[:])

# 用切片的方式来传递函数
# 如果 想输出打印模型而不想让原本的未打印模型清空的话，可以用切片副本来参与到函数内
print_models(unprinted_designs[:],completed_models)