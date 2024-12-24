# 10.1
import json
from pathlib import Path

# 读取路径
path = Path('learning_python.txt')

contents = path.read_text().rstrip()
print(contents,end='\n\n')

lines = contents.splitlines()
for line in lines:
	print(line)

# 10.2
# replace() 字符串内单词的替换
contents.replace('Python','C')

# 10.3
# 简化代码 尽量去删除临时变量

# lines = contents.splitlines()
# for line in lines:
# 	print(line)

for line in contents.splitlines():
	print(line)

# 10.4 & 10.5
from pathlib import Path

# 用列表来存储名字，后续在将其转化为字符串来转化过来
names = []

while True:
	name = input("请输入你的名字，你按'q'键就可以退出输入：")
	if name == 'q':
		break
	else:
		names.append(name)

# 将 列表names 转换为 换行字符串
name_str = '\n'.join(names)

path = Path('guest.txt')
path.write_text(name_str)

# 10.6 & 10.7
print('请输入两个数字，如果你不想输入了可以按“q”来退出')

while True:
	first_number = input('第一个数是：')
	if first_number == 'q':
		break
	try:
		first_number_int = int(first_number)
	except ValueError:
		print('请不要输入非数字！')
		continue

	second_number = input('第二个数是：')
	if second_number == 'q':
		break
	try:
		second_number_int = int(second_number)
	except ValueError:
		print('请不要输入非数字！')
		continue

	print(f"两数之和是{first_number_int + second_number_int}")


# 10.8 & 10.9
pass

# 10.10
# count() 可以看出单词在字符串中出现的次数
from pathlib import Path

path = Path('gudengbao.txt') # 未下载

contents_words = path.read_text().split()

print(contents_words.lower().count('then'))
print(contents_words.lower().count('there'))
print(contents_words.lower().count('the '))

# 10.11 & 10.12
from pathlib import Path
import json

def get_favorite_number(path):
	""" """
	number = input('请输入你喜欢的数：')
	contents = json.dumps(number)
	path.write_text(contents)
	print(f"I know your favorite number! It's {number}")

path = Path('fav_number.json')
get_favorite_number(path)

# 10.13
from pathlib import Path
import json

def get_stored_username(path):
	""" 和上面的基础操作是一致的 如果存在 输出名字 """
	if path.exists():
		contents = path.read_text()
		use_info = json.loads(contents)
		return use_info
	else:
		return None

# 丰富
def get_new_username(path):
	""" 录入新的名字 """
	username = input(f'请输入你的名字：')
	age = input(f'请输入你的年龄：')
	usr_info = {'username':username,'age':age}
	contents = json.dumps(usr_info)
	path.write_text(contents)
	return usr_info

# 主函数 内嵌 上面函数
def greet_user():
	""" 1 """
	path = Path('usr_info.json')
	use_info = get_stored_username(path) # 调用上部函数
	if use_info:
		active = input(f'你的用户名是{use_info['username']}吗？'
					   f'如果是输入y，如果不是输入n')
		if active =='y':
			print(f'欢迎回来，{use_info['username']},你的年龄是{use_info['age']}')
		elif active =='n':
			return get_new_username(path)

		else:
			print('请输入正确的形式')
			greet_user()
	else:
		use_info = get_new_username(path)
		print(f'我将记住你,{use_info['username']},你的年龄是{use_info['age']}')

path = Path('usr_info.json')
get_new_username(path)
get_stored_username(path)

greet_user()


