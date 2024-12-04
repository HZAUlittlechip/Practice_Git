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
     # 可以用join()将数列中元素连接合并成为一个字符串 ！ 且join只用于字符串的合并
invite_message = ", ".join(invite_person) # ", "来分隔元素
print(f"{invite_message} will be invite to attend our party.")

# 练习 3.6：添加嘉宾 你刚找到了⼀张更⼤的餐桌，可容纳更多的嘉宾
# 就座。请想想你还想邀请哪三位嘉宾。
# 以完成练习 3.4 或练习 3.5 时编写的程序为基础，在程序末尾添加函数
# 调⽤ print()，指出你找到了⼀张更⼤的餐桌。
# 使⽤ insert() 将⼀位新嘉宾添加到名单开头。
# 使⽤ insert() 将另⼀位新嘉宾添加到名单中间。
# 使⽤ append() 将最后⼀位新嘉宾添加到名单末尾。
# 打印⼀系列消息，向名单中的每位嘉宾发出邀请。

new_man = ['Mike','Marry','Tom']
invite_person.insert(0,new_man[0])
invite_person.insert(3,new_man[1])
invite_person.append(new_man[2])
invite_message = ", ".join(invite_person)
print(f"{invite_message} will be invite to attend our party.")

# 练习 3.7：缩短名单 你刚得知新购买的餐桌⽆法及时送达，因此只能
# 邀请两位嘉宾。
# 以完成练习 3.6 时编写的程序为基础，在程序末尾添加⼀⾏代码，
# 打印⼀条你只能邀请两位嘉宾共进晚餐的消息。
# 使⽤ pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为⽌。
# 每次从名单中弹出⼀位嘉宾时，都打印⼀条消息，让该嘉宾知道
# 你很抱歉，⽆法邀请他来共进晚餐。
# 对于余下两位嘉宾中的每⼀位，都打印⼀条消息，指出他依然在
# 受邀之列。
# 使⽤ del 将最后两位嘉宾从名单中删除，让名单变成空的。打印
# 该名单，核实名单在程序结束时确实是空的

print(f"{invite_message}, Sorry, I can just invite two person.")
run_man = invite_person.pop()
print(f"Sorry,{run_man},You can not attend my party.")
run_man = invite_person.pop()
print(f"Sorry,{run_man},You can not attend my party.")
run_man = invite_person.pop()
print(f"Sorry,{run_man},You can not attend my party.")
run_man = invite_person.pop()
print(f"Sorry,{run_man},You can not attend my party.")
print(invite_person)
new_invite_messgae = ", ".join(invite_person)
print(f"{invite_person[0]},You can attend the party")
print(f"{invite_person[1]},You can attend the party")
del invite_person[0] # del一次只能删除一个元素
del invite_person[0]
print(invite_person)



