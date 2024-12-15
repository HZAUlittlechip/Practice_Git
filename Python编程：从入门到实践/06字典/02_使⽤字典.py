# 在 Python 中，字典（dictionary）是⼀系列键值对。每个键都与⼀个值关
# 联，可以使⽤键来访问与之关联的值。与键相关联的值可以是数、字符
# 串、列表乃⾄字典。

# 键值对包含两个相互关联的值。
# 键和值之间⽤冒号分隔，⽽键值对之间⽤逗号分隔

# 6.2.1 访问字典中的值
alien_0 = {'color': 'green'}
print(alien_0['color'])

alien_0 = {'color': 'green', 'points': 5}
print(f"You just earned {alien_0['points']} points!")

# 6.2.2 添加键值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

# 字典添加键值
alien_0['x_position'] = 0
alien_0['y_position'] = 25

# 6.2.3 从创建⼀个空字典开始
# 在空字典中添加键值对很⽅便，甚⾄是必需的。
alien_0 = {}             # 创建一个空的键值，到时可以根据实际情况来插入键值
alien_0['color'] = 'green'
alien_0['point'] = 5

# 6.2.4 修改字典中的值
alien_0['color'] = 'yellow'
# 一个有趣的列子---来表示外星人的移动情况
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

#  输出原始位置
print(f'the original x_position is : {alien_0['x_position']}')

# 根据不同的速度模式来修改位移的距离
if alien_0['speed'] == 'slow':
	x_incrmement = 1
elif alien_0['speed'] == 'medium':
	x_incrmement = 2
else :
	x_incrmement = 3

# 更新修改位置坐标
alien_0['x_position'] = alien_0['x_position'] + x_incrmement

print(alien_0['x_position'])

# 6.2.5 删除键值对
# del ...
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# 6.2.6 由类似的对象组成的字典
favorite_languages = {
	'jen': 'python',
	'sarch': 'c',
	'edward': 'rust',
	'pill': 'python'
}

# 6.2.7 使⽤ .get() 来访问值
alien_0 = {'color': 'green', 'speed': 'slow'}
# .get( ) 第一个参数---用与指定键；第二个参数---若指定键不存在时返回的内容
# 因为如果我们直接输出字典内不含的键时，程序会报错而无法继续进行
point_value = alien_0.get('point', 'No point value')
