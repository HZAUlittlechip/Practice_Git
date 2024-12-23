# 10.1
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

