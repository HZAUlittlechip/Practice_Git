# 函数json

# 10.4.1 使⽤ json.dumps() 和 json.loads()
from pathlib import Path
import json
import os


numbers = [2, 3, 5, 7, 11, 13]

path = Path('number.json')

# 将输入的列表用json的格式来进行保存在json文件中
# json.dumps()
contents = json.dumps(numbers)
path.write_text(contents)

# 来读取json中的文件 json.loads()
path = Path('number.json')
contents = path.read_text()
numbers = json.loads(contents) # 解码 contents

print(numbers)

# 10.4.2 保存和读取⽤户⽣成的数据

# json 和 write_txt 和 input 的联动
from pathlib import Path
import json

# 将用户输入的名字存在文档里面

name = input('请输入你的名字：')

path = Path('username.json')	# 存储为json的格式
contents = json.dumps(name)		# 转化 为json统一格式
path.write_text(contents)		# 写入内容

# 读取 json文件中的内容并输出语句
user = path.read_text() 		# path路径已经存在直接读取就可以
user_json = json.loads(user)	# path 保存的格式为 WindowsPath

print(f'{user_json}你好')

## 小项目
# 这个程序运⾏时，将尝试从内存中获取⽤户的⽤户名。如果没有找到，就提⽰⽤户输 ⼊⽤户名，
# 并将其存储到⽂件 username.json 中，以供下次使⽤。

from pathlib import Path
import json

# 判断 用户名 是否存在
path = Path('username.json')
# 存在 读取文件 且输出问候语言
if path.exists():
	contents = path.read_text()
	username = json.loads(contents)
	print(f'欢迎回来，{username}')
# 不存在 写入文件 且也输出问候语
else:
	username = input('请输入你的名字：')
	contents = json.dumps(username)
	path.write_text(contents)
	print(f'我将记住你{username}')

# 10.4.3 重构
# 将 复杂的函数 重构 为不同简单的小函数

def greet_user():
	""" 问候用户的函数 """
	from pathlib import Path
	import json

	# 判断 用户名 是否存在
	path = Path('username.json')
	# 存在 读取文件 且输出问候语言
	if path.exists():
		contents = path.read_text()
		username = json.loads(contents)
		print(f'欢迎回来，{username}')
	# 不存在 写入文件 且也输出问候语
	else:
		username = input('请输入你的名字：')
		contents = json.dumps(username)
		path.write_text(contents)
		print(f'我将记住你{username}')

## 缩减上面的函数

# 单独来定义一个 存储用户名的函数
from pathlib import Path
import json

def get_stored_username(path):
	""" 和上面的基础操作是一致的 如果存在 输出名字 """
	if path.exists():
		contents = path.read_text()
		username = json.loads(contents)
		return username
	else:
		return None

def get_new_username(path):
	""" 录入新的名字 """
	username = input(f'请输入你的名字：')
	contents = json.dumps(username)
	path.write_text(contents)
	return username

# 主函数 内嵌 上面函数
def greet_user():
	""" 1 """
	path = Path('username.json')
	username = get_stored_username(path) # 调用上部函数
	if username:
		print(f'欢迎回来，{username}')
	else:
		get_new_username(path)
		print(f'我将记住你,{username}')

greet_user()
