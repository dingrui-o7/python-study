# 变量和字符串
name = 'dingrui'        # 字符串变量
print(f'hello {name}')  # 输出 f 字符串


# 在字符串中添加空白
# \t: 在字符串中表示制表符。
# \n: 在字符串中表示换行符。
print('Python Rust')
print()
print('Python\tRust')  # 使用制表符
print()
print('Python\nRust')  # 使用换行符


# 字符串的常见方法
# title(): 将每个单词的首字母都改为大写。
# upper()/lower(): 将字符串全部改为大写/小写。
# rstrip()/lstrip()/strip(): 移除字符串右端/左端/两端的空白。
# removeprefix(val)/removesuffix(val): 移除字符串中指定的前缀/后缀
# 在一行中给多个变量赋值
msg1, msg2 = 'hello world', ' dingrui'
print(f'{msg1.title()}\n{msg1.upper()}')
print(f'{msg2}\n{msg2.strip()}')
print('fname.txt'.removesuffix('.txt'))


# 整数值、浮点数（小数）值、布尔值
# Python使用下划线而不是逗号来作为千位分隔符
print(1, 1_000_000, 1.5)
print(True, False)  # 布尔值
print(1 + 1, 1.0 + 1.0, 1 + 1.0)
# 乘方、除法、整除法（向下取整）和求模
print(3 ** 2, 3 / 2, 3 // 2, 5 % 2)