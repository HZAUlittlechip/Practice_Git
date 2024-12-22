class Restaurant:
	""" 模拟餐厅的具体情况 """
	def __init__(self,restaurant_name,cuisine_type):
		""" 初始化 类 的名称和餐饮类型"""
		self.name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f'我们餐厅的名称是{self.name}')
		print(f'我们餐厅有的食物有{self.cuisine_type}')

	def open_restaurant(self):
		print('餐厅正在营业')

	def member_restaurant(self):
		print(f'{self.number_served}人已经在此就餐了')

	# 添加 传递函数 生成新的加入的人
	def set_number_served(self,member):
		self.number_served = member

	# 添加 增加函数 加上新加入的人
	def increment_number_served(self,incr_member):
		self.number_served += incr_member

class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type,flavors):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors = flavors

	def describe_flavors(self):
		""" 用来描述冰淇淋的口味 """
		print(f'我们的冰淇淋口味有',end='')
		for flavor in self.flavors:
			print(flavor,end=' ')