# 练习 8.1：消息 编写⼀个名为 display_message() 的函数，让它
# 打印⼀个句⼦，指出本章的主题是什么。调⽤这个函数，确认显⽰的
# 消息正确⽆误。

def display_message():
	""" 打印本章的主题 """
	print('本章的主题是函数')

display_message()

# 练习 8.2：喜欢的书 编写⼀个名为 favorite_book() 的函数，其
# 中包含⼀个名为 title 的形参。让这个函数打印⼀条像下⾯这样的消
# 息。
# One of my favorite books is Alice in Wonderland.
# 调⽤这个函数，并将⼀本书的书名作为实参传递给它。

def  favorite_book(title):
	""" 输入你喜欢的书 """
	print(f'One of my favorite books is {title}')

favorite_book('JOKER')

# 练习 8.3：T 恤 编写⼀个名为 make_shirt() 的函数，它接受⼀个
# 尺码以及要印到 T 恤上的字样。这个函数应该打印⼀个句⼦，简要地
# 说明 T 恤的尺码和字样。
# 先使⽤位置实参调⽤这个函数来制作⼀件 T 恤，再使⽤关键字实参来
# 调⽤这个函数


def make_shirt(size,word):
	print(f'这件衣服的尺码是{size}，上面的字样是{word}')

# 位置参数
make_shirt(36,'Just do it!')

# 关键词参数
make_shirt(word='Just do it!',size= 36)

# 练习 8.4：⼤号 T 恤 修改 make_shirt() 函数，使其在默认情况下
# 制作⼀件印有
# “I love Python”字样的⼤号 T 恤。调⽤这个函数分别制作⼀件印有默认
# 字样的⼤号 T 恤，⼀件印有默认字样的中号 T 恤，以及⼀件印有其他
# 字样的 T 恤（尺码⽆关紧要）。

def make_shirt(size,word = 'I love python'):
	print(f'这件衣服的尺码是{size}，上面的字样是{word}')

# 大号 T
make_shirt('big')

# 中号 I
make_shirt('medium')

# 别的字样
make_shirt('medium',word= '嘿嘿')

# 练习 8.5：城市 编写⼀个名为 describe_city() 的函数，它接受
# ⼀座城市的名字以及该城市所属的国家。这个函数应该打印⼀个像下
# ⾯这样简单的句⼦。
# Reykjavik is in Iceland.
# 给⽤于存储国家的形参指定默认值。为三座不同的城市调⽤这个函
# 数，其中⾄少有⼀座城市不属于默认的国家

def describe_city(city_name, counrty = 'China'):
	print(f'{city_name} is in {counrty}')

describe_city('wuhan')
describe_city('dalian')
describe_city('xiaoliucheng',counrty= 'xiaoliuguo')

# 练习 8.6：城市名 编写⼀个名为 city_country() 的函数，它接受
# 城市的名称及其所属的国家。这个函数应返回⼀个格式类似于下⾯的
# 字符串：
# "Santiago, Chile"
# ⾄少使⽤三个城市⾄国家对调⽤这个函数，并打印它返回的值

def city_country(city_name,country_name):
	print(f'{city_name.title()}, {country_name.title()}')

# 练习 8.7：专辑 编写⼀个名为 make_album() 的函数，它创建⼀个
# 描述⾳乐专辑的字典。这个函数应接受歌⼿名和专辑名，并返回⼀个
# 包含这两项信息的字典。使⽤这个函数创建三个表⽰不同专辑的字
# 典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。

def make_album(singer_number,sing_number):
	""" 构建歌手和歌名的字典 """
	singer_inf = {
		'name': singer_number,
		'sing': sing_number
	}
	return singer_inf

zhuanji = make_album('liuzihuan',1)
print(zhuanji)
zhuanji2 = make_album('liuzihuan',2)
print(zhuanji2)
zhuanji3 = make_album('liuzihuan',3)
print(zhuanji3)

# 练习 8.8：⽤户的专辑 在为练习 8.7 编写的程序中，编写⼀个 while
# 循环，让⽤户输⼊歌⼿名和专辑名。获取这些信息后，使⽤它们来调
# ⽤ make_album() 函数并将创建的字典打印出来。在这个 while 循
# 环中，务必提供退出途径。
def make_album(singer_number,sing_number):
	""" 构建歌手和歌名的字典 """
	singer_inf = {
		'name': singer_number,
		'sing': sing_number
	}
	return singer_inf

while True:
	print('请输入歌手名 和 专辑名字')
	print('退出按‘q’')

	name = input('请输入歌手名字：')
	if name == 'q':
		break

	sing = input('请输入专辑的名称：')
	if sing == 'q':
		break

	sing_information = make_album(name,sing)
	print(sing_information)

# 练习 8.9：消息 创建⼀个列表，其中包含⼀系列简短的⽂本消息。将
# 这个列表传递给⼀个名为 show_messages() 的函数，这个函数会打
# 印列表中的每条⽂本消息。

def show_message(messages):
	for message in messages:
		print(message)

messages = ['1','2','3','4']
show_message(messages)

# 练习 8.10：发送消息 在为练习 8.9 编写的程序中，编写⼀个名为
# send_messages() 的函数，将每条消息都打印出来并移到⼀个名为
# sent_messages 的列表中。调⽤ send_messages() 函数，再将两
# 个列表都打印出来，确认把消息移到了正确的列表中。


def send_messages(messages, sended_message):
	while messages:
		message = messages.pop()
		print(f'{message}已经发送')
		sended_message.append(message)

messages = ['1','2','3','4']
sended_message = []

send_messages(messages,sended_message)
print(messages)
print(sended_message)




