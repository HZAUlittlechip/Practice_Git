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