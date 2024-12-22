# 导入类
# 从文件 car.py中导出

import sys
sys.path.append("C:\\Users\刘子桓\PycharmProjects\practice\Python编程：从入门到实践\\09类")

from car import Car
my_car = Car('audi','a8','2024')

print(my_car.get_descriptive_name())
my_car.read_odometer()

# 9.4.3 从⼀个模块中导⼊多个类
	# from car import Car, Ele

# 或者导入整个模块
import car
my_mustang = car.Car('ford', 'mustang', 2024)
# 还是用car.Car的形式导入指定的类 【模块名.类名】


# 导入模块内的所有类
from car import *

# 9.4.6 在⼀个模块中导⼊另⼀个模块

# 分别从每个模块导入类
from car import Car
from  electric_car import Ele_car

# 9.4.7 使⽤别名
# 同 函数 的调用 as