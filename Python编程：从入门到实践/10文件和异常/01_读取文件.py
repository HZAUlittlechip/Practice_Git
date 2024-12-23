# 10.1.1 读取⽂件的全部内容
# pathlib 模块
from pathlib import Path
import sys

sys.path.append(r"C:\Users\刘子桓\PycharmProjects\practice\
					Python编程：从入门到实践\10文件和异常")

# 导入文件时先看控制台当前的控制路径是哪
import os
print(os.getcwd()) # 输出当前控制台路径
# 修改目前python的默认运行路径
os.chdir(r"C:\Users\刘子桓\PycharmProjects\practice\Python编程：从入门到实践")


path = Path('pi_digits.txt')
# read_text() 函数来读取文件内容
# 读取文件是其都默认为 字符串 的形式进行保存，若要修改 需要用到 int() , float()
contents = path.read_text()
print(contents)

# .rstrip() 删除 读取文档的空行
# contents = contents.rstrip()

# 方法链式的手法
contents = path.read_text().rstrip()

# 相对路径 和 绝对路径

# 10.1.3 访问⽂件中的各⾏
# splitlines() 将字符串转为一系列的行
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()

# 对读取的数据进行换行
lines = contents.splitlines()	# 列表的形式
for line in lines:
	print(line,end='')

# 10.1.4 使⽤⽂件的内容

## 将读取的数据进行转换存储
pi_str = ''
for line in lines:
	pi_str += line.lstrip()  # 字符串的相加

print(pi_str)

# 10.1.5 包含 100 万位的⼤型⽂件
