# 在控制台输出的话要 额外添加 路径来不然会报错
# import sys
# sys.path.append("C:\\Users\刘子桓\PycharmProjects\practice\Python编程：从入门到实践\\08函数")

# 8.6.1 导⼊整个模块
# 导入文件，其中可以包含文件中的函数 和 包
import cheese
cheese.make_pizza(16, 'one')

# 8.6.2 导⼊特定的函数
# from module_name import function_name

from cheese import make_pizza
cheese.make_pizza(16, 'one')

# 8.6.3 使⽤ as 给函数指定别名
# 可指定 简短⽽独⼀⽆⼆的别名（alias）
from cheese import make_pizza as mp

mp(16,'one')

# 8.6.4 使⽤ as 给模块指定别名
import cheese as c

c.make_pizza(16, 'one')

# 8.6.5 导⼊模块中的所有函数 添加 *
from cheese import *
