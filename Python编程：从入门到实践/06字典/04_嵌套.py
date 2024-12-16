# 嵌套

# 6.4.1 字典列表
# 在列表中 嵌套 字典
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# 创建列表字典
aliens = [alien_0, alien_1, alien_2]

# 输出列表
for alien in aliens:
	print(alien)

# *** 同时返回索引和键值
# enumerate()  作用于可迭代对象（如列表、元组、字符串等)
for index, alien in enumerate(aliens): # 索引是0，1，2
	print(f'Alien {index}：{alien}')

# 外星人项目
aliens = []

# 创建30个绿色外星人
for alien_number in range(0,30):  # 程序循环执行30次
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# 显示前5个外星人
for alien in aliens[0:5]:  # [start:end]
	print(alien)

# 显示创建了多少个外星人
print(f'目前已经创建了{len(aliens)}个外星人')

# 将前三个外星⼈修改为⻩⾊、速度中等且值 10 分，可这样做
# 循环 提取出前三个外星人
for alien in aliens[0:3]:

# 如果外星人的颜色为绿色就对机器人的属性进行修改
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

# 显示前5个外星人
for alien in aliens[0:5]:
	print(alien)

# 6.4.2 在字典中存储列表

# 披萨案例
# 存储了⽐萨两个⽅⾯的信息：外⽪类型 和 配料列表
# 存储顾客需要的披萨信息
pizza = {
		'crust': 'thick',
		 'toppings': ['mushrooms', 'extra cheese'], # 注意末尾是有,的
}

# 输出需要的披萨信息
print(f'你需要的披萨皮是{pizza['crust']},你添加的配料是{pizza['toppings']}')
# 输出的topping是带方框的列表形式

# 正确输出
print(f'你需要的披萨皮是{pizza['crust']},你添加的配料是')

# 循环输出配料的名称
for topping in pizza['toppings']:
	print(topping)  # 输出的配料名称会自动换行，可以用,end=" " 来取消默认的换行

# print(f'你需要的披萨皮是{pizza['crust']},你添加的配料是', end= "")
# for topping in pizza['toppings']:
# 	print(topping, end= " ")

# 6.4.3 在字典中存储字典
users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
	},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
	},
}

# 输出形如
#Username: aeinstein
#  Full name: Albert Einstein
#  Location: Princeton

# 遍历大字典
for user_name, user_info in users.items():
	print(f'Username: {user_name}')
	full_name = f'{user_info['first'].title()} {user_info['last']} '
	location  = user_info['location']

	print(f'\tFull name: {full_name}')
	print(f'\tLocation: {location}')