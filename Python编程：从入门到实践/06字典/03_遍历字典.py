### 6.3.1 遍历所有的键值对
# 用户的名字信息
user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }

# 遍历寻找输出键 和 值
# .item()
for key, value in user_0.items():	# key 和 value 这两个变量的定义任意的
	print(f'\nkey: {key}')
	print(f'value: {value}')

### 6.3.2 遍历字典中的所有键
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

for name in favorite_languages.keys():	#  .keys()
	print(f'name: {name}')

# 在遍历字典时，会默认遍历所有的键 （不带值）
# 所以 for name in favorite_languages.keys(): 等价于
for name in favorite_languages:
	print(f'name: {name}')

#  6.3.3 按特定的顺序遍历字典中的所有键
#  对字典中的键盘进行分类---sorted()
#  其也是对变量临时修改的函数
sorted(favorite_languages.keys()) # ['edward', 'jen', 'phil', 'sarah']
print(favorite_languages.keys()) # dict_keys(['jen', 'sarah', 'edward', 'phil'])

# 6.3.4 遍历字典中的所有值
# .values()
print(favorite_languages.values())

# *set()集合函数的建立
# 提出重复项，确保元素独一无二
# 同样不会修改原来的字典
set(favorite_languages.values()) # {'python', 'rust', 'c'}

# 集合的建立 可以直接用一个 {}
languages = {'python', 'rust', 'python', 'c'}
print(languages) 	# {'python', 'rust', 'c'}

