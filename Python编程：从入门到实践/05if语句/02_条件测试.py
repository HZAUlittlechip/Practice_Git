# 每条 if 语句的核⼼都是⼀个值为 True 或 False 的表达式，这种表达式
# 称为 条件测试。
# if 是条件测试语句

# 5.2.1 检查是否相等
car = 'bmw'
car == 'bmw'
	# car == 'audi' False

# 5.2.2 如何在检查是否相等时忽略⼤⼩写
car = 'Audi'
car.lower()

# 5.2.3 检查是否不等
requested_topping = 'mushrooms'
if requested_topping != 'water':
	print("give me a water~")

# 5.2.4 数值⽐较
	# 简单的大于小于号

# 5.2.5 检查多个条件
# 01 and 检查多个文件 是 且 的关系
# 要检查两个条件是否都为 True，可使⽤关键字 and 将两个条件测试合⽽为⼀。
age1 = 18
age2 = 20
age1 <= 30 and age2 <= 30
age1 <= 30 and age2 <= 19  # (age1 <= 30) and (age2 <=19)

# 02. 使⽤ or 检查多个条件 是 并 的关系
age1 <= 30 or age2 <= 19

# 5.2.6 检查特定的值是否在列表中
# ... in ...
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings

# 5.2.7 检查特定的值是否不在列表中
# ... not in ...
'water' not in requested_toppings  # True

