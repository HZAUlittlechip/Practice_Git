def name_formatted(first,last,middle=''):
	""" 格式化姓名 """
	if middle:
		full_name = f'{first} {middle} {last}'
	else:
		full_name = f'{first} {last}'
	return full_name.title()