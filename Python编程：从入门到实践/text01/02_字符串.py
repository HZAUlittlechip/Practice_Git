# String
from pyexpat.errors import messages

name = "add lovelace"
print(name.title()) # title() 首字母大写
print(name.upper()) # 全大写
print(name.lower()) # 全小写

# 在字符串中插⼊变量的值
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" # f(format)字符串
print(full_name)
print(f"Hello,{full_name.title()}!")
message = f"Hello, {full_name.title()}!"

# 使⽤制表符\t或换⾏符\n来添加空⽩
print("\tpython") #制表
print("Languages:\npython\nC\nJavascript")

# 删除空白 rstrip()  用户信息处理
language = "python   "
print(language)
print(language.rstrip()) # rstrip 函数的删除空白是暂时的，需重新更新变量
language = language.rstrip()

# 删除前缀 removeprefix()
url = "hello,world!"
print(url.removeprefix("hello,")) # World!

# 如何在使⽤字符串时避免语法错误
