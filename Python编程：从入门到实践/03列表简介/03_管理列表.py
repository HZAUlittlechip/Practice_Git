# 调整表格的顺序
# 感受临时函数和永久函数的区别

# 3.3.1 使⽤ sort() ⽅法对列表进⾏ 永久排序
# 字母全小写的情况 .lower()函数
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) #按字⺟顺序排列的

cars.sort(reverse= True) #字母反方向排列
print(cars)

# 3.3.2 使⽤ sorted() 函数对列表进⾏ 临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
rank_cars = sorted(cars)
print(rank_cars)
print(cars)

# 3.3.3 反向打印列表
# reverse()
cars.reverse()
print(cars)

# 3.3.4 确定列表的⻓度
# len()
a = len(cars)
print(a)

