# exception （错误）
from sys import excepthook

# traceback 报告错误

# ZeroDivisionError
# 分母为 0 的情况

# 10.3.2 try - expect 代码块
try:
	print(5/0)
except ZeroDivisionError:
	print('请不要让分母为零')

# 10.3.3 使⽤异常避免崩溃
print("给我两个数，我会将他们进行除法运算：")
print("如果你想退出的话请按“q”")

while True:
	first_number = input('第一个数字：')
	if first_number == 'q':
		break

	second_number = input('第二个数字：')
	if second_number == 'q':
		break

	answer = int(first_number)/int(second_number)

	print(answer) # 输入分母为 0 的情况会报错

# 利用 else 代码块 来在结果try：结果正确无误的情况输出结果
print("给我两个数，我会将他们进行除法运算：")
print("如果你想退出的话请按“q”")

while True:
	first_number = input('第一个数字：')
	if first_number == 'q':
		break

	second_number = input('第二个数字：')
	if second_number == 'q':
		break

	try:
		answer = int(first_number)/int(second_number)
	except ZeroDivisionError:
		print('第二个数字不要输入零')
	else:
		print("%.2f" %answer) # 输入分母为 0 的情况会报错

# 10.3.5 处理 FileNotFoundError 异常

# 判断 traceback 的错误 最好从最结尾的部分来开始看 --> 可以看 except 针对哪个部分

from pathlib import Path

path = Path('alice.txt')
try:
	contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
	print(f"Sorry, the file {path} does not exist.")

# 分析文本
from pathlib import Path

path = Path('learning_python.txt')

# 防止错误用try来帮助程序不崩溃
try:
	contents = path.read_text()
except:
	print(f'无法在本路径下找到文件{path}')
# 将文本内的字符都分割成 单个单词 用 split() 含糊
else:
	words = contents.split()
	print(f'这个文本的单词的个数为{len(words)}')

# 10.3.7 使⽤多个⽂件
# 定义函数批量 用循环批量处理需要分析的文本

# 10.3.8 静默失败
# 在expect Error： 里面只添加 Pass




