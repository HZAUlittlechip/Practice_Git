class User:
	""" 用户信息的私人定制 """
	def __init__(self,first_name,last_name,age,home):
		self.first = first_name
		self.last = last_name
		self.age = age
		self.home = home
		self.login_attempts = 0

	def describe_user(self):
		""" 个人信息的介绍 """
		print(f'全名为{self.first.title()} {self.last}')
		print(f'年龄为:{self.age}')
		print(f'家位于：{self.home.title()}')

	def greet_user(self):
		""" 问候客户 """
		print(f'你好，{self.first.title()} {self.last}')

	# 增加 login_attempts
	def increment_login_attempts(self):
		self.login_attempts += 1

	# 重置 login_attempts
	def reset_login_attempts(self):
		self.login_attempts = 0

class Privileges:
	""" 管理权限的类 """
	def __init__(self):
		self.privileges = ['can add post', 'can delete', 'can ban user']

	def show_privileges(self):
		""" 展示管理员的权限 """
		print('管理员的权限有：')
		for privilege in self.privileges:
			print(privilege)

class Admin(User):
	""" 管理员的类 """
	def __init__(self,first_name,last_name,age,home):
		super().__init__(first_name,last_name,age,home)

		self.privileges = Privileges()
