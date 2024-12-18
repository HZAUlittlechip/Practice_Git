# 7.3.1 在列表之间移动元素

# 有⼀个列表包含新注册但还未验证的⽹站⽤户。验证这些⽤户后，如
# 何将他们移到已验证⽤户列表中呢？

# 使⽤⼀个 while 循环，在验证⽤户的同时将其从未验证⽤户列表中提取出来，
# 再将其加⼊已验证⽤户列表

# 未验证用户
unconfirmed_users = ['alice', 'brian', 'candace']

# 已验证用户
confirmed_users = []

# 验证全部用户
while unconfirmed_users:
	confirmed_user = unconfirmed_users.pop()

# 将用户添加在已验证用户中
	print(f'恭喜{confirmed_user}已成功验证')
	confirmed_users.append(confirmed_user)

# 分别输出已经验证的用户
print('\n以下用户已经被验正')
for confirmed_user in confirmed_users:
	print(confirmed_user)

# 7.3.2 删除为特定值的所有列表元素

# 删除里面全部 cat
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')
print(pets)

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

remove_pet = set(pets)
print(remove_pet)

# 7.3.3 使⽤⽤户输⼊填充字典

# 利用 while 循环 来将 用户 和 用户消息 填充到字典中

# 创建一个用户消息的空字典
responses = {}
# 创建标志
poll_active = True
# 循环过程
while poll_active:
	name = input('请输入你的名字：')
	response = input('你最喜欢的山是哪座山')
# 将输入的信息存入字典中
	responses[name] = response
	# 跳出循环条件
	reject = input('是否还询问参加的人数呢？不询问了输入‘no’')
	if reject == 'no':
		poll_active = False
# 调查结果的输出
for name, response in responses.items():
	print(f'{name}参加了本次活动，它想去的山是{response}')

