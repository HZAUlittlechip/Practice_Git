# 可以处理⼀些数据，并返回⼀个或⼀组 值。函数返回的值称为 返回值

# 处理一个人名并且返回其名字
def get_formatted_name(first_name,last_name):
	""" 输入名和姓 且返回其姓名"""
	full_name = f'{first_name} {last_name}'
	return  full_name.title()

man = get_formatted_name('liu','zihuan')
print(man)

# 8.3.2 让实参变成可选的

# 添加 中间的名字 而有些人没有中间的名字如何处理呢？
# ***让中间名变成可选的，可给形参 middle_name 指定默认值（空字符串）***
def get_formatted_name(first_name,last_name,middle_name = ''):
	""" 输入名和姓 且返回其姓名，如果有中间名就也输出中间名"""
	if middle_name:
		full_name = f'{first_name} {middle_name} {last_name}'
	else:
		full_name = f'{first_name} {last_name}'
	return  full_name.title()

man = get_formatted_name('liu','zihuan')
print(man)

man = get_formatted_name('liu','zihuan','xiao')
print(man)

# 8.3.3 返回字典
def build_person(first_name, last_name):
	"""返回⼀个字典，其中包含有关⼀个⼈的信息"""
	person = {'first': first_name, 'last': last_name}
	return person

musician = build_person('jimi', 'hendrix')
print(musician)

# 添加 空的数值类名称来供用户信息
def build_person(first_name, last_name,age = None):
	""" 返回⼀个字典，其中包含有关⼀个⼈的信息, 年龄是选填项 """
	person = {
		'first': first_name,
		'last' : last_name,
	}

	# 判断 年龄是否输入了
	if age:
		person['aga'] = age
	return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# 8.3.4 结合使⽤函数和 while 循环
# 用户可以在想要的时候退出，且 按q 退出
def get_name(first_name,last_name):
	"""处理姓和名 """
	full_name = f'{first_name} {last_name}'
	return full_name.title()

# active = True active 无法保证 其随时可以退出，不如条件语句用break退出
while True:
	print('请输入你的姓名')
	print('你可以在任何输入时间按‘q’退出')

	# 用户输入姓名 且 想退出的时候就判断条件
	f_name = input('请输入你的姓：')
	if f_name == 'q':
		break

	l_name = input('请输入你的名：')
	if l_name == 'q':
		break

	name = get_name(f_name,l_name)
	print(f'Hello, {name}')



