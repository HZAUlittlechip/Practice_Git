# 4.3.1 使⽤ range() 函数
for value in range(1,5):
    print(value) # 列排列的 1234 不会输出5
for value in range(6):
    print(value)

# 4.3.2 使⽤ range() 创建数值列表
# list()
numbers = list(range(6))
print(numbers)

# range(begin, end, path_length)
ever_number = list(range(2,11,2))
print(ever_number)

# EX：如何创建⼀个列表，其中包含前 10 个整数（1〜10）的平⽅？
squares = []
for value in range(1,11): # range() 来遍历数值或者数据
    square = value ** 2
    squares.append(square) # squares.append(value**2)
print(squares)


# 4.3.3 对数值列表执⾏简单的统计计算
# max() ; min() ; sum()
print(max(squares))
print(min(squares))
print(sum(squares))

# 4.3.4 列表推导式
squares = [value**2 for value in range(1,11)]
print(squares)

