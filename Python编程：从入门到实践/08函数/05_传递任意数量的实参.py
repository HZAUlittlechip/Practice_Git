# *行参 不管调⽤语句提供了多少实参，这个形参都会将其收⼊囊中

def make_pizza(*toppings): # *toppings 创建 元组来扩展储存的信息
	"""打印顾客点的所有配料"""
	print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 8.5.1 结合使⽤位置实参和任意数量的实参

# Python 先匹配位置实参和关键字实参，再将余下的实参都收集到最后⼀个形参中。
# 例：
# def make_pizza(size, *toppings):

# 8.5.2 使⽤任意数量的关键字实参
# 遇到，不知道实参数量 和 不知道实参会传递什么信息的 情况
# **行参 --- 字典 可以无限添加键对
def build_profile(first,last,**user_info):
	user_info['first name'] = first
	user_info['last name'] = last
	return user_info

user_profile = build_profile('albert','einstein',location = 'princetion'
							 , field = 'physic')
# # 后面是将两个键对传递给了**user——info

print(user_profile)