# 位置参数 和 关键字参数

# 8.2.1 位置实参

# Python 必须将函数调⽤中的每个实参关联到函数定义中的 ⼀个形参。
# 最简单的⽅式是基于实参的顺序进⾏关联

# 宠物 的种类和名称
def describe_pet(animal_type, pet_name):
	"""显⽰宠物的信息"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

# 01. 调⽤函数多次
describe_pet('hamster', 'harry')
describe_pet('cat', 'tom')

# 02. 位置实参的顺序很重要

# 8.2.2 关键字实参

def describe_pet(animal_type, pet_name):
	"""显⽰宠物的信息"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type= 'hamster',pet_name= 'harry')

# 设置默认值

# 默认值的参数要放在无默认值形参后面
# python 按顺序将 第一个实参 连接到 第一个行参
def describe_pet(pet_name, animal_type = 'dog'):
	"""显⽰宠物的信息"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry')

# 默认值 可以在调用时修改
describe_pet(pet_name='harry', animal_type='hamster')

# 8.2.4 等效的函数调⽤
