# 以 格式化 名字的函数为例，来看pytest包是如何运行的
import sys
import os
sys.path.append(r'C:\Users\刘子桓\PycharmProjects\practice'
		 r'\Python编程：从入门到实践\11测试代码')
os.chdir(r'C:\Users\刘子桓\PycharmProjects\practice'
		 r'\Python编程：从入门到实践\11测试代码')


from name_function import name_formatted

print("Enter 'q' at any time to quit.")
while True:
	first = input("\nPlease give me a first name: ")
	if first == 'q':
		break
	last = input("Please give me a last name: ")
	if last == 'q':
		break

	formatted_name = name_formatted(first, last)
	print(f"\tNeatly formatted name: {formatted_name}.")
