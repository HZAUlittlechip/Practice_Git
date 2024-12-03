# 练习 2.1：简单消息 将⼀条消息赋给变量，并将其打印出来
message_for_mi = "LOVE YOU!"
print(message_for_mi)

# 练习 2.2：多条简单消息 将⼀条消息赋给变量，并将其打印出来；再
# 将变量的值修改为⼀条新消息，并将其打印出来。
message_for_mi = "LOVE YOU!"
print(message_for_mi)
message_for_mi = "I LOVE YOU SO MUCH!"
print(message_for_mi)

# 练习 2.3：个性化消息 ⽤变量表⽰⼀个⼈的名字，并向其显⽰⼀条消
# 息。显⽰的消息应⾮常简单，如下所⽰。
name = "Eric"
print(f"Hello {name}, would you like to learn some Python today?")

# 练习 2.4：调整名字的⼤⼩写 ⽤变量表⽰⼀个⼈的名字，再分别以全
# ⼩写、全⼤写和⾸字⺟⼤写的⽅式显⽰这个⼈名。
all_daxie = name.upper()
all_xiaoxie = name.lower()
firstzimudaxie = name.title()
print(all_xiaoxie)
print(all_daxie)
print(firstzimudaxie)

# 练习 2.5：名⾔ 1 找到你钦佩的名⼈说的⼀句名⾔，将这个名⼈的姓
# 名和名⾔打印出来。输出应类似于下⾯这样（包括引号）。
print('Albert Einstein once said, "A person who never made a mitake '
      'never tried anything new."')  #用单引号来包双引号不会报错

# 练习 2.6：名⾔ 2 重复练习 2.5，但⽤变量 famous_person 表⽰名
# ⼈的姓名，再创建要显⽰的消息并将其赋给变量 message，然后打印
# 这条消息。
famous_person = "Albert Einstein"
message = '"A person who never made a mitake never tried anything new"'
print(f"{famous_person} once said, {message}")

# 练习 2.7：删除⼈名中的空⽩ ⽤变量表⽰⼀个⼈的名字，并在其开头
# 和末尾都包含⼀些空⽩字符。务必⾄少使⽤字符组合 "\t" 和 "\n" 各
# ⼀次。
love_person = "\tMi\nGuiyin\t"
print(love_person)
love_person1 = love_person.lstrip()
print(love_person1)
love_person2 = love_person1.rstrip()
print(love_person2)
love_person3 = love_person2.strip()
print(love_person3)

# 练习 2.8：⽂件扩展名 Python 提供了 removesuffix() ⽅法，其⼯
# 作原理与 removeprefix() 很像。请将值 'python_notes.txt'
# 赋给变量 filename，再使⽤ removesuffix() ⽅法来显⽰不包含
# 扩展名的⽂件名，就像⽂件浏览器所做的那样。
filename = "python_notes.txt"
#去除后缀用removesuffix() ; 去除前缀用removeprefix() 他们搜索的方向不一样
filename_without_extension = filename.removesuffix(".txt")
print(filename_without_extension)

# 练习 2.9：数字 8 编写 4 个表达式，分别使⽤加法、减法、乘法和除
# 法运算，但结果都是数字 8。为了使⽤函数调⽤ print() 来显⽰结
# 果，务必将这些表达式⽤括号括起来。也就是说，你应该编写 4 ⾏类
# 似于这样的代码：print(5+3)
print(2+6)
print(12-4)
print(2*4)
print(64/8)

# 练习 2.10：最喜欢的数 ⽤⼀个变量来表⽰你最喜欢的数，再使⽤这
# 个变量创建⼀条消息，指出你最喜欢的数是什么，然后将这条消息打
# 印出来。
favorite_number = 12
favorite_number = f"my favorite number is {favorite_number}."
print(favorite_number)

# 小结
# 在本章中，你⾸先学习了如何使⽤变量，如何创建描述性变量名，以及如
# 何消除名称错误和语法错误。然后学习了字符串是什么，以及如何使⽤全
# ⼩写、全⼤写和⾸字⺟⼤写的⽅式显⽰字符串。你使⽤空⽩来显⽰整洁的
# 输出，还学习了如何删除字符串中多余的字符。你接着学习了如何使⽤整
# 数和浮点数，了解了⼀些使⽤数值数据的⽅式。你还学习了如何编写说明
# 性注释，让代码对你和其他⼈来说更容易理解。最后，你了解了让代码尽
# 可能简单的理念