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
