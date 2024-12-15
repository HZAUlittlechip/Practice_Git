#  5.4.1 检查特殊元素
#  输出需要的配料列表
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	print(f'add {requested_topping}')

print('\n That is all')

# 缺少材料是输出无材料 （内嵌if语句）
# 如果green peppers用完了
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("No green peppers")
	else:
		print(f'add {requested_topping}')

print('\n That is all')

# 5.4.2 确定列表⾮空
# 对于数值 0、空值 None、单引号空字符串 ''、双引号空字符串 ""、空列表 []、空元组 ()、空
# {}，Python 都会返回 False。
requested_toppings = [] # 创建一个空列表
if requested_toppings:  # 检验是否为空集，为空集（false）就跳入else
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}.")
	print("\nFinished making your pizza!")
else:


# 5.4.3 使⽤多个列表
# 检查顾客需要的配料是否在总配料表内
available_toppings = ['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese'] #总配料表定义
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
# "french fires"没有
if requested_toppings:
	for requested_topping in requested_toppings:
		if requested_topping not in available_toppings:
			print(f'{requested_topping} not have')
		else:
			print(f'you need{requested_topping} in the pizza')

	print(f'\n you pizza will coming soon')
else:
	print("Are you sure you want a plain pizza?")