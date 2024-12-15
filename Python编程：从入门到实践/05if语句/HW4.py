# 练习 5.3：外星⼈颜⾊ 1 假设玩家在游戏中消灭了⼀个外星⼈，请创
# 建⼀个名为 alien_color 的变量，并将其赋值为
# 'green'、'yellow' 或 'red'。
alien_colors = ['green', 'yellow', 'red']
alien_color = 'green'

# 编写⼀条 if 语句，测试外星⼈是否是绿⾊的。如果是，就打印⼀
# 条消息，指出玩家获得了 5 分。
if alien_color == 'green':
	print('gain 5 points!')
# 编写这个程序的两个版本，上述条件测试在其中的⼀个版本中通
# 过，在另⼀个版本中未通过（未通过条件测试时没有输出）
if alien_color == 'green':
	print('gain 5 points!')
else:
	print()

# 练习 5.4：外星⼈颜⾊ 2 像练习 5.3 那样设置外星⼈的颜⾊，并编写
# ⼀个 if-else 结构。
alien_color = 'green'
# alien_color = 'red'
if alien_color ==  'green':
	print("yes")
else:
	print("no")

# 练习 5.5：外星⼈颜⾊ 3 将练习 5.4 中的 if-else 结构改为 ifelif-else 结构。
if alien_color ==  'green':
	print("5 points")
elif alien_color == 'yello':
	print("10 points")
else:
	print("15 points")

#练习 5.6：⼈⽣的不同阶段 设置变量 age 的值，再编写⼀个
# if-elif-else 结构，根据 age 的值判断这个⼈处于⼈⽣的哪个阶段。
age = 77
who_are_you = '0'

if age < 2:
	who_are_you = 'baby'
elif age >= 2 and age < 4:
	who_are_you = 'little_child'
elif age >= 4 and age < 13:
	who_are_you = 'child'
elif age >= 13 and age < 18:
	who_are_you = 'teenager'
elif age <= 18 and age <65 :
	who_are_you = 'middle_man'
else:
	who_are_you = 'old_man'

print(f"This guy is a {who_are_you}.")

# 练习 5.7：喜欢的⽔果 创建⼀个列表，其中包含你喜欢的⽔果，再编
# 写⼀系列独⽴的 if 语句，检查列表中是否包含特定的⽔果。
# 将该列表命名为 favorite_fruits，并让其包含三种⽔果。
favorite_fruits = ['apple', 'banana', 'beer']
favorite_fruit = 'banana'
if 'banana' in favorite_fruits:
	print('yes')

# 练习 5.8：以特殊⽅式跟管理员打招呼
# 创建⼀个⾄少包含 5 个⽤户名
# 的列表，并且其中⼀个⽤户名为 'admin'。想象你要编写代码，在每
# 个⽤户登录⽹站后都打印⼀条问候消息。遍历⽤户名列表，向每个⽤
# 户打印⼀条问候消息。
user_names = ['admin','one','two','three','four']
for user_name in user_names:
	if user_name == 'admin':
		print("Hello admin, would you like to see a status report?")
	else:
		print(f'Hello {user_name}, thank you for logging in again.')

# 练习 5.9：处理没有⽤户的情形 在为练习 5.8 编写的程序中，添加⼀
# 条 if 语句，检查⽤户名列表是否为空。
user_names = ['admin','one','two','three','four']
if user_names:
	for user_name in user_names:
		if user_name == 'admin':
			print("Hello admin, would you like to see a status report?")
		else:
			print(f'Hello {user_name}, thank you for logging in again.')
else:
	print('We need to find some users!')

# 练习 5.10：检查⽤户名 按照下⾯的说明编写⼀个程序，模拟⽹站如
# 何确保每个⽤户的⽤户名都独⼀⽆⼆。
# 创建⼀个⾄少包含 5 个⽤户名的列表，并将其命名为
# current_users。
# 再创建⼀个包含 5 个⽤户名的列表，将其命名为 new_users，并
# 确保其中有⼀两个⽤户名也在列表 current_users 中。
# 遍历列表 new_users，检查其中的每个⽤户名是否已被使⽤。如
# 果是，就打印⼀条消息，指出需要输⼊别的⽤户名；否则，打印
# ⼀条消息，指出这个⽤户名未被使⽤。
# 确保⽐较时不区分⼤⼩写。换句话说，如果⽤户名 'John' 已被
# 使⽤，应拒绝⽤户名 'JOHN'。（为此，需要创建列表
# current_users 的副本，其中包含当前所有⽤户名的全⼩写版本。）
current_users = ['admin','one','two','three','four']
new_users = ['One','two','five','six','seven']
# 错误转换全小写的方式： current_users_lower = current_users.lower()
# .lower()函数无法直接作用于列表，只能作用单个字符串！得用循环重新复制给列表
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
	if new_user.lower() in current_users_lower:
		print(f"输入别的用户名,{new_user} 已经被使用")
	else:
		print("该用户名未被使用")

# 练习 5.11：序数 序数表⽰顺序位置，如 1st 和 2nd。序数⼤多以 th 结
# 尾，只有 1st、2nd、3rd 例外。
numbers = [value for value in range(1,10)]
for number in numbers:
	if number == 1:
		print(f'{number}st')
	elif number == 2:
		print(f'{number}nd')
	elif number == 3:
		print(f'{number}rd')
	else:
		print(f'{number}th')

# 在本章中，你⾸先学习了如何编写结果要么为 Ture、要么为 False 的条
# 件测试。然后学习了如何编写简单的 if 语句、if-else 语句和 if_elif-else 语句。
# 在程序中，可以使⽤这些结构来测试特定的条件，以确
# 定这些条件是否满⾜。你接着学习了在使⽤ for 循环⾼效处理列表元素
# 时，如何对某些元素做特殊处理。你还再次学习了 Python 在代码格式⽅⾯
# 提出的建议。遵循这些建议，即便你编写的程序越来越复杂，其代码也依
# 然易于阅读和理解。
# 在第 6 章中，你将学习 Python 字典。字典类似于列表，但能够让你将不同
# 的信息关联起来。你还将学习如何创建和遍历字典，以及如何将字典与列
# 表和 if 语句结合起来使⽤。学习字典让你能够模拟现实世界中的更多情形