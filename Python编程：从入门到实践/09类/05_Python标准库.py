from random import randint
from random import choice

# 生成 1 - 6 之间的随机数
i = randint(1,6)

# 从 元组 或者 列表 中随机抽取元素
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)