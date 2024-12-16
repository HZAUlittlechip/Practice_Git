# 练习 6.1：⼈ 使⽤⼀个字典来存储⼀个⼈的信息，包括名、姓、年龄
# 和居住的城市。该字典应包含键 first_name、last_name、age 和
# city。将存储在该字典中的每项信息都打印出来

myself = {'first_name': 'Liu', 'last_name': 'zihuan','age': 23,'city':'WuHan'}
print(myself)

# 练习 6.2：喜欢的数 1 使⽤⼀个字典来存储⼀些⼈喜欢的数。请想出
# 5 个⼈的名字，并将这些名字⽤作字典中的键。再想出每个⼈喜欢的⼀
# 个数，并将这些数作为值存储在字典中。打印每个⼈的名字和喜欢的
# 数。为了让这个程序更有趣，通过询问朋友确保数据是真实的。
favorite_numbers = {
	'mine': 12,
	'mi': 10,
	'tan': 8,
	'lv': 12,
	'mom': 7
}

# 练习 6.3：词汇表 1 Python 字典可⽤于模拟现实⽣活中的字典。为避
# 免混淆，我们将后者称为词汇表。

# 想出你在前⾯学过的 5 个编程术语，将它们⽤作词汇表中的键，
# 并将它们的含义作为值存储在词汇表中。
word_list = {
	'code': '编码',
	'function': '函数',
	'block': '块',
	'dictionary': '字典',
	'slice': '切片'
}

# 练习 6.4：词汇表 2 现在你知道了如何遍历字典，请整理你为练习 6.3
# 编写的代码，将其中的⼀系列函数调⽤ print() 替换为⼀个遍历字典
# 中键和值的循环。确保该循环正确⽆误后，再在词汇表中添加 5 个
# Python 术语。当你再次运⾏这个程序时，这些新术语及其含义将⾃动
# 包含在输出中。

# .items()同时输出
for word_key, word_value in word_list.items():
	print(f'{word_key}\t{word_value}')

# 输出键
for word_key in word_list.keys():
	print(f'The key is {word_key}')

# 输出值
for word_value in word_list.values():
	print(f'The value is {word_value}')

# 添加5个python词汇
word_list['set'] = '集合'
word_list['number'] = '数字'
word_list['pile'] = '桩'
word_list['sheet pile'] = '板桩'
word_list['engineer'] = '工程师'

# 遍历字典
for word_translate in word_list.items():
	print(word_translate)

# 练习 6.5：河流 创建⼀个字典，在其中存储三条河流及其流经的国
# 家。例如，⼀个键值对可能是 'nile': 'egypt'。
# 使⽤循环为每条河流打印⼀条消息，如下所⽰。
# The Nile runs through Egypt.

rivers = {
	'nile': 'nanfei?',
	'egypt': 'baixi?',
	'Yangzi': 'China'
}

for river_number in rivers.keys():
	print(f'The {river_number } runs through {rivers[river_number]}')

# 练习 6.6：调查 在 6.3.1 节编写的程序 favorite_languages.py 中执⾏以
# 下操作。
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

# 创建⼀个应该会接受调查的⼈的名单，其中有些⼈已在字典中，
# ⽽其他⼈不在字典中。

# 创建邀请人名单
invite_persons = ['jen', 'liu', 'trump']
invite_persons_keys =\
	[invite_persons_name for invite_persons_name in favorite_languages.keys()]

for invite_person in invite_persons:
	# 如果参与调查输出感谢你的调查
	if invite_person in invite_persons_keys:
		print(f"{invite_person}感谢你的调查")
	else:
		print(f"{invite_person}请你参加我们的调查")

# 练习 6.7：⼈们 在为练习 6.1 编写的程序中，再创建两个表⽰⼈的字
# 典，然后将这三个字典都存储在⼀个名为 people 的列表中。遍历这
# 个列表，将其中每个⼈的所有信息都打印出来。
myself = {'first_name': 'Liu', 'last_name': 'zihuan','age': 23,'city':'WuHan'}
xiaomi = {'first_name': 'Mi', 'last_name': 'guiyin','age': 25,'city':'Rizhao'}
xiaoning = {'first_name': 'Lv', 'last_name': 'jinning','age': 25,'city':'GanZhou'}

peoples = [myself, xiaomi, xiaoning]

for people in peoples:
	name = f'{people['first_name']} {people['last_name']}'
	age = people['age']
	city = people['city']

	print(f'姓名：{name}, 年龄：{age},居住城市：{city}')

# 练习 6.8：宠物 创建多个表⽰宠物的字典，每个字典都包含宠物的类
# 型及其主⼈的名字。将这些字典存储在⼀个名为 pets 的列表中，再
# 遍历该列表，并将有关每个宠物的所有信息打印出来。
# ********* 同上 **********

# 练习 6.9：喜欢的地⽅ 创建⼀个名为 favorite_places 的字典。
# 在这个字典中，将三个⼈的名字⽤作键，并存储每个⼈喜欢的 1〜3 个
# 地⽅。为让这个练习更有趣些，让⼀些朋友说出他们喜欢的⼏个地
# ⽅。遍历这个字典，并将其中每个⼈的名字及其喜欢的地⽅打印出
# 来。
favorite_places = {
	'my':['wuhan','wuhan','wuhan'],
	'he':['caidian','caidian'],
	'she':['jiedao']
}

# 输出分别输出名字和喜欢的地方
for name, places in favorite_places.items():
	print(name,end='')
	place = ','. join(places)  # 将字符串连来一起 ",".join()
	print(f'喜欢位置是{place}') # map(str,) 可以将数值型的转换为字符串

# 练习 6.10：喜欢的数 2 修改为练习 6.2 编写的程序，让每个⼈都可以
# 有多个喜欢的数字，然后将每个⼈的名字及其喜欢的数打印出来。
# ***** 同上 *****

# 练习 6.11：城市 创建⼀个名为 cities 的字典，将三个城市名⽤作
# 键。对于每座城市，都创建⼀个字典，并在其中包含该城市所属的国
# 家、⼈⼝约数以及⼀个有关该城市的事实。表⽰每座城市的字典都应
# 包含 country、population 和 fact 等键。将每座城市的名字以及
# 相关信息都打印出来。

# 字典中带字典
cities = {
	'wuhan' : {'country': 'China','population':1000,'fact': 'big'},
	'rizhao' : {'country': 'China','population':100,'fact': 'mid'},
	'xingguo' : {'country': 'China','population':10,'fact': 'small'}
}

# 输出 城市名称 和 所处位置 人口数 事件
for city_name, city_info in cities.items():
	print(city_name,end='')
	print(f'位于{city_info['country'].title()}，'
		  f'它的人口有{city_info['population']}万人,'
		  f'它比较{city_info['fact']}')

# *** 本章小结
# 在本章中，你⾸先学习了如何定义字典，以及如何使⽤存储在字典中的信
# 息。然后学习了如何访问和修改字典中的元素，以及如何遍历字典中的所
# 有信息。接着学习了如何遍历字典中的所有键值对、所有的键和所有的
# 值。你还学习了如何在列表中嵌套字典，如何在字典中嵌套列表，以及如
# 何在字典中嵌套字典。