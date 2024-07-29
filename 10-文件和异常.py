# 读写文件
from pathlib import Path
path = Path('msg.txt')
path.write_text('Hello DingRui!\nHappy coding!')

contents = path.read_text()
print(len(contents.splitlines()))
print(contents)


# 异常
# 异常是 Python 创建的特殊对象，用于管理程序运行时出现的错误。
try:
    num = int(input("Type is a number "))
    answer = 5 + num
except ValueError:
    print("You must type a number!")
else:
    print(answer)
finally:
    print("Exit.")


# 序列化（json 库）
import json

numbers = [2, 3, 5, 7, 11, 13]
contents = json.dumps(numbers)
numbers_load = json.loads(contents)
print(contents, numbers_load == numbers)