# 练习 5.3：外星⼈颜⾊ 1 假设玩家在游戏中消灭了⼀个外星⼈，请创
# 建⼀个名为 alien_color 的变量，并将其赋值为
# 'green'、'yellow' 或 'red'。
alien_colors = ['green', 'yellow', 'red']
alien_color = 'green'

# 编写⼀条 if 语句，测试外星⼈是否是绿⾊的。如果是，就打印⼀
# 条消息，指出玩家获得了 5 分。
if alien_color == 'green':
	print('gain 5 points!')
# 编写这个程序的两个版本，上述条件测试在其中的⼀个版本中通
# 过，在另⼀个版本中未通过（未通过条件测试时没有输出）
if alien_color == 'green':
	print('gain 5 points!')
else:
	print()

# 练习 5.4：外星⼈颜⾊ 2 像练习 5.3 那样设置外星⼈的颜⾊，并编写
# ⼀个 if-else 结构。
alien_color = 'green'
# alien_color = 'red'
if alien_color ==  'green':
	print("yes")
else:
	print("no")

# 练习 5.5：外星⼈颜⾊ 3 将练习 5.4 中的 if-else 结构改为 ifelif-else 结构。
if alien_color ==  'green':
	print("5 points")
elif alien_color == 'yello':
	print("10 points")
else:
	print("15 points")

#练习 5.6：⼈⽣的不同阶段 设置变量 age 的值，再编写⼀个
# if-elif-else 结构，根据 age 的值判断这个⼈处于⼈⽣的哪个阶段。
age = 77
who_are_you = '0'

if age < 2:
	who_are_you = 'baby'
elif age >= 2 and age < 4:
	who_are_you = 'little_child'
elif age >= 4 and age < 13:
	who_are_you = 'child'
elif age >= 13 and age < 18:
	who_are_you = 'teenager'
elif age <= 18 and age <65 :
	who_are_you = 'middle_man'
else:
	who_are_you = 'old_man'

print(f"This guy is a {who_are_you}.")

# 练习 5.7：喜欢的⽔果 创建⼀个列表，其中包含你喜欢的⽔果，再编
# 写⼀系列独⽴的 if 语句，检查列表中是否包含特定的⽔果。
# 将该列表命名为 favorite_fruits，并让其包含三种⽔果。
favorite_fruits = ['apple', 'banana', 'beer']
favorite_fruit = 'banana'
if 'banana' in favorite_fruits:
	print('yes')