""" 注意文档开头是以test_开头的 """

#  测试函数 name_formatted 是否符合标准
from name_function import name_formatted

def test_name_longlonglong():  # 测试函数名应该比一般函数要长
	formatted_name = name_formatted('janis','joplin')
	assert formatted_name == 'Janis Joplin'

# 编写完测试代码 -- > 去终端输入pytest即可开始测试
def test_first_last_middle_name():
	formatted_name = name_formatted('wolfgang','mozart','amadeus')
	assert formatted_name == 'Wolfgang Amadeus Mozart'