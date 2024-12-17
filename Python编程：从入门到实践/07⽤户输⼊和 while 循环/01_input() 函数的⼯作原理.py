# input()

# input() 函数的⼯作原理
# input() 函数让程序暂停运⾏，等待⽤户输⼊⼀些⽂本。
# 且程序会将输入理解为 字符串
message = input('Tell me something, and I will repeat it back to you:')
print(message) # 输入的内容被赋予给了message

# 7.1.1 编写清晰的提⽰
# 要帮助用户知道要填写哪些内容！

# 请输入你的名字
name = input('请输入你的名字：')
print(f'你好，{name}')

# 提示的内容过长时，可先将提⽰赋给⼀个变量，再将这个变量传递给 input() 函数
prompt = ("If you share your name, we can personalize the messages you "
		  "see.")  # 直接在后面添加 \nWhat is your name? 也可以
# += 运算符追加字符串在末尾
prompt += '\nWhat is your name?'

name = input(prompt)
print(f'你好，{name}')

# 7.1.2 使⽤ int() 来获取数值输⼊
# 用int()函数来将 字符串 转换为 数字形式

# 如果在int里面内嵌input其输出的的值是 你输入的数值 程序不会中断。
# height = int(input("How tall are you, in inches? "))

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
 print("\nYou're tall enough to ride!")
else:
 print("\nYou'll be able to ride when you're a little older.")

# 7.1.3 求模运算符 ^^^ % ^^^
4 % 4  # 0
4 % 5  # 4
4 % 3  # 1

# 可利⽤这⼀点来判断⼀个数是奇数还是偶数
number = input("Enter a number, and I'll tell you if it's even or odd:"
			   "")
number = int(number)  # int 只会对输入的值变成整型！ 而不会对前面生成的字符串产生影响

if number % 2 == 0:
	print(f'{number}是偶数')
else:
	print(f'{number}是奇数')


