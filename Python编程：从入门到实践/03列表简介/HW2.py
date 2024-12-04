# 练习 3.1：姓名 将⼀些朋友的姓名存储在⼀个列表中，并将其命名为
# names。依次访问该列表的每个元素，从⽽将每个朋友的姓名都打印
# 出来。
from pyexpat.errors import messages

name = ['Mi Guiyin','Lv jingning','Tan zikang']
print(f"{name[0]} {name[1]} {name[2]}")

# 练习 3.2：问候语 继续使⽤练习 3.1 中的列表，但不打印每个朋友的
# 姓名，⽽是为每⼈打印⼀条消息。每条消息都包含相同的问候语，但
# 抬头为相应朋友的姓名。
message = 'GOOD MORNRING! '
print(f"{name[0]}, {message}")
message1 = message + name[0] # 以字符串的形式储存
print(message1)

# 练习 3.3：⾃⼰的列表 想想你喜欢的通勤⽅式，如骑摩托⻋或开汽
# ⻋，并创建⼀个包含多种通勤⽅式的列表。根据该列表打印⼀系列有
# 关这些通勤⽅式的陈述，如下所⽰ I would like to own a Honda motorcycle.
style = ['walk','bus','texi']
print(f"I love {style[0]} after my lunch!")

# 练习 3.4：嘉宾名单 如果你可以邀请任何⼈⼀起共进晚餐（⽆论是在
# 世的还是故去的），你会邀请哪些⼈？请创建⼀个列表，其中包含⾄
# 少三个你想邀请的⼈，然后使⽤这个列表打印消息，邀请这些⼈都来
# 与你共进晚餐。
invite_person =  ['Mi Guiyin','Lv jingning','Tan zikang','jorker']
print(f"invite {invite_person[0]}, {invite_person[1]} and {invite_person[2]} for dinner.")

# 练习 3.5：修改嘉宾名单 你刚得知有位嘉宾⽆法赴约，因此需要另外
# 邀请⼀位嘉宾。
# 以完成练习 3.4 时编写的程序为基础，在程序末尾添加函数调⽤
# print()，指出哪位嘉宾⽆法赴约。
# 修改嘉宾名单，将⽆法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
# 再次打印⼀系列消息，向名单中的每位嘉宾发出邀请。

sick_person = invite_person.pop()
print(f"{sick_person} is sick, can not be attend out party")
new_person = 'Mike'
     # new_invite_person = invite_person.append(new_person)
     # invite_person.append(new_person) 不会返还最后生成的数列，而是返还None

     # print(f"{invite_person[0,1,2]} will be invite to attend our party.")
     # 可以用join()将数列中元素连接合并成为一个字符串 ！
invite_message = ", ".join(invite_person) # ", "来分隔元素
print(f"{invite_message} will be invite to attend our party.")

