from pathlib import Path


# write_txt()
path = Path('programming.txt')
path.write_text('I love programming')

# 10.2.2 写⼊多⾏

# 用 += 来追加字符串
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path.write_text(contents)



