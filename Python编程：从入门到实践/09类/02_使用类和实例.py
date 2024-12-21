# 9.2.1 Car 类
class Car:
	""" 描述一款汽车的基本配置"""
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0  # 可日后修改的固定参数

	def get_descriptive_name(self):
		"""返回格式规范的描述性信息"""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""打印⼀条指出汽⻋⾏驶⾥程的消息"""
		print(f"This car has {self.odometer_reading} miles on it.")


my_car = Car('audi','a8','2024')
print(my_car.get_descriptive_name())
my_car.read_odometer()

## 9.2.3 修改属性的值

# 以修改 汽车的里程 odometer_reading 为例子
# 01. 直接修改属性的值

my_car.odometer_reading = 23
my_car.read_odometer()

# 02. 通过⽅法修改属性的值
# 在原有的类中添加一个方法
def update_odometer(self,mileage):
	""" 更新里程值 """
	# 添加一个有趣的规则来让 里程表 无法向回调
	# 如果 修改值 大于 初始的 正常返回
	if mileage >= self.odometer_reading:
		self.odometer_reading = mileage
	else:
		print('请不要回调里程表')

my_car = Car('audi','a8','2024')
my_car.update_odometer(66)
print(my_car.read_odometer())

# 03. 通过⽅法让属性的值递增
def increase_odometer(self, increase):
	""" 更新里程值 """
	self.odometer_reading += increase


