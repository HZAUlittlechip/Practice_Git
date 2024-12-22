# 父类 和 子类

# 比如 汽车 和 电动车

# 超类 super() 可以用来调用 父类的方法！

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

	def update_odometer(self, mileage):
		""" 更新里程值 """
		# 添加一个有趣的规则来让 里程表 无法向回调
		# 如果 修改值 大于 初始的 正常返回
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print('请不要回调里程表')

	def increase_odometer(self, increase):
		""" 更新里程值 """
		self.odometer_reading += increase

# 新建一个电动车的子类
class Ele_car(Car):
	""" 电动车部分"""
	def __init__(self,make,model,year,owner): # owner 是父类没有的
		""" 定义电动车自己的属性 """
		# super(). 继承父类中的 方法
		super().__init__(make,model,year) # 说明这三个参数是复制的父类的

### 9.3.2 给⼦类定义属性和⽅法
		self.owner = owner
		self.battery_size = 40

	def describe_battery(self):
		print(f'电池的容量还有{self.battery_size}')

	def owner_car(self):
		print(f'这辆车的主人是{self.owner}')

### 9.3.3 重写⽗类中的⽅法
	# 可以重新定义一个和父类重名的函数来替代 或者说是重写 父类 中的 方法

my_leaf = Ele_car('nissan','leaf','2024','me')
print(my_leaf.get_descriptive_name())

my_leaf.owner_car()
my_leaf.describe_battery()


# 9.3.4 将实例⽤作属性
# 将大的类 细分成小的类

# 如 发现 电车的中的方式太多了，不如单独分出一个类来，比如说电池的类
# 就可以在 电车的上级再生成一个电池的类，来让电车来引用
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

my_leaf = Ele_car('nissan','leaf',2024) # my_leaf -- self -- instance

print(my_leaf.get_descriptive_name())  # 需要调用父类Car
my_leaf.battery.describe_battery()  #  先调用battery 然后调用Battery赋予给它的函数

# 9.3.5 模拟实物


