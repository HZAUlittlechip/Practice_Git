# 函数json

# 10.4.1 使⽤ json.dumps() 和 json.loads()
from pathlib import Path
import json
import os


numbers = [2, 3, 5, 7, 11, 13]

path = Path('number.json')

# 将输入的列表用json的格式来进行保存在json文件中
# json.dumps()
contents = json.dumps(numbers)
path.write_text(contents)

# 来读取json中的文件 json.loads()
path = Path('number.json')
contents = path.read_text()
numbers = json.loads(contents) # 解码 contents

print(numbers)

# 10.4.2 保存和读取⽤户⽣成的数据