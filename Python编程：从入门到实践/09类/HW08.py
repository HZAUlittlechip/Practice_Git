# 练习 9.1：餐馆 创建⼀个名为 Restaurant 的类，为其
# __init__() ⽅法设置两个属性：restaurant_name 和
# cuisine_type。创建⼀个名为 describe_restaurant() 的⽅法
# 和⼀个名为 open_restaurant() 的⽅法，其中前者打印前述两项信
# 息，⽽后者打印⼀条消息，指出餐馆正在营业。
# 根据这个类创建⼀个名为 restaurant 的实例，分别打印其两个属
# 性，再调⽤前述两个⽅法。

class Restaurant:
	""" 模拟餐厅的具体情况 """
	def __init__(self,restaurant_name,cuisine_type):
		""" 初始化 类 的名称和餐饮类型"""
		self.name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f'我们餐厅的名称是{self.name}')
		print(f'我们餐厅有的食物有{self.cuisine_type}')

	def open_restaurant(self):
		print('餐厅正在营业')

restaurant = Restaurant('liuxiaohuan','hot dry noodles')

restaurant.describe_restaurant()
restaurant.open_restaurant()

# 练习 9.2：三家餐馆 根据为练习 9.1 编写的类创建三个实例，并对每
# 个实例调⽤ describe_restaurant() ⽅法。
yours = Restaurant('mixiaoyin','one')
hers = Restaurant('lvxiaoning','two')

yours.describe_restaurant()
hers.describe_restaurant()

# 练习 9.3：⽤户 创建⼀个名为 User 的类，其中包含属性
# first_name 和 last_name，还有⽤户简介中通常会有的其他⼏个
# 属性。在类 User 中定义⼀个名为 describe_user() 的⽅法，⽤于
# 打印⽤户信息摘要。再定义⼀个名为 greet_user() 的⽅法，⽤于向
# ⽤户发出个性化的问候。
# 创建多个表⽰不同⽤户的实例，并对每个实例调⽤上述两个⽅法。

class User:
	""" 用户信息的私人定制 """
	def __init__(self,first_name,last_name,age,home):
		self.first = first_name
		self.last = last_name
		self.age = age
		self.home = home

	def describe_user(self):
		""" 个人信息的介绍 """
		print(f'全名为{self.first.title()} {self.last}')
		print(f'年龄为:{self.age}')
		print(f'家位于：{self.home.title()}')

	def greet_user(self):
		""" 问候客户 """
		print(f'你好，{self.first.title()} {self.last}')


user1 = User('liu','zihuan',23,'wuhan')

user1.describe_user()
user1.greet_user()
