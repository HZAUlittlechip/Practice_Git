# 列表是什么？
# 难道和数组是一类的？是矩阵吗？
from pyexpat.errors import messages

# 列表通常包含多个元素，因此给列表指定⼀个表⽰复数的名称（如 letters、digits 或names）是个不错的主意。

# []表示列表；，来分割其间元素 ; 是有序集合
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles) # 放在控制台中读取会显示他的 元素位置0-3 和 列表长度_len_

# 3.1.1 访问列表元素 输出列表中元素
print(bicycles[1]) # cannondale
print(bicycles[1].title())

# 3.1.2 索引从 0 ⽽不是 1 开始
# 返回最后一个元素
print(bicycles[-1]) # 等价于print(bicycles[3])
print(bicycles[-2])

#3.1.3 使⽤列表中的各个值
messages = f"My first bicycles was a {bicycles[1].title()}."
print(messages)