# 讲一个模块导入另一个模块
""" 电动车 类块 """

from car import Car

class Battery:
	"""  电车电池的类 """
	def __init__(self,battery_size = 40):
		""" 初始化电池的容量 """
		self.battery_size =  battery_size

	def describe_battery(self):
		print(f'电池的容量还有{self.battery_size}')

# 重新编写精简版 的电动车类
class Ele_car(Car):
	""" 精简版电车类 """
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		# 创建一个新的 Battery 实例 来在Ele_car中被应用
		# 其也属于初始化的过程
		self.battery = Battery()

