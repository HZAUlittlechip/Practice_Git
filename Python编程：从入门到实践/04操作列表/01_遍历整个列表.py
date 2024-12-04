# 循环的引言

# 4.1.1 深⼊研究循环
magicians = ['alice', 'david', 'carolina']
for magician in magicians:  #从列表 magicians 中取出⼀个名字，并将其与变量magician 相关联
    print(magician)

# 4.1.2 在 for 循环中执⾏更多的操作
print(magician) # 根据上面的for循环，最后赋予的magician的词是最后一个元素carolina
for magician in magicians:
    print(f"{magician.title()}, was a good trick.")
    print(f"I can't wait to see your next trick,"
          f"{magician.title()}.\n")

# 4.1.3 在 for 循环结束后执⾏⼀些操作
# 在 for 循环后⾯，没有缩进的代码都只执⾏⼀次，不会重复执⾏。