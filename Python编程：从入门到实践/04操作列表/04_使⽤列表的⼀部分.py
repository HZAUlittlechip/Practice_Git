# 4.4.1 切⽚ (slice)
players = ['charles', 'martina', 'michael', 'florence', 'eli']

# [begin:end]索引的解释
# 从begin的索引开始到end前索引结束
# EX：[0:3] 遍历到的索引为0, 1, 2

# 输出的仍然为列表的形式
print(players[0:3]) # 提取第1到第3个元素
print(players[1:4]) # 提取第2到第4个元素
print(players[:])  # 提取全部元素
print(players[1:]) # 从第2个开始提取元素
print(players[:3]) # 提取到第3个元素结束

print(players[-3:]) #从倒数第3个元素来提取

# 4.4.2 遍历切⽚
# EX：遍历输出前三个运动员的姓名
print("Hera are the first three player on my team:")
for name in players[:3]:
    print(name)

# 4.4.3 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
# friend_food = ny_food 是错误的，必须使用切片，两个变量会指向同一个链表
# 导致无法进行后续的修改，且两个变量修改增加会同时进行

my_foods.append('ice cream')
friend_foods.append('hamburger')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)