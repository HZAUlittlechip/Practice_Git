def make_pizza(size, *toppings):
	"""概述要制作的⽐萨"""
	print(f"\nMaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")

import os
import sys
print("工作目录:", os.getcwd())
print("模块路径:", sys.path)
