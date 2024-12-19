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