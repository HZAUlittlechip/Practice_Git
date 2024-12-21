# OOP 面向对象编程

# 编写表⽰现实世界中的 事物 和 情景 的类（class）
# 且基于这些 类 来创造 对象(object)

# 根据类来创建对象称为实例化，这让你能够使⽤类的实例（instance）。

# 下⾯来编写⼀个表⽰⼩狗的简单类 Dog
# ——它表⽰的不是特定的⼩狗，⽽是 任何⼩狗。

### 9.1.1 创建 Dog 类

# 小狗们 两项信息（名字和年龄）和两种⾏为（坐下和打滚）

# 类 的首字母大写

# __init__(self,) method  是两个下划线

# 开始创建 dog 类
# 使用类的人无法看到类内部函数
class Dog:
	""" 模拟小狗 """
	def __init__(self,name,age):
		""" 初始化 姓名 和 年龄 """
		self.name = name
		self.age = age

	def sit(self):
		""" 模拟小狗 收到命令会坐下"""
		print(f'{self.name} is now sitting')

	def roll_over(self):
		""" 模拟小狗 打转"""
		print(f'{self.name} rolled over')

# 9.1.2 根据类创建实例 (my dog)

my_dog = Dog('willie',6)
your_dog = Dog('Jack',3)

print(f"my dog's name is {my_dog.name}")
print(f"your dog's age is {your_dog.age}")

# 使用类中的函数
my_dog.sit()
my_dog.roll_over()





