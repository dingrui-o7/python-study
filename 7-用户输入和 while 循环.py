# 用户输入
name = input("Please enter your name: ")
print(f"\nHello, {name}")


# 字符串转换其他类型
# int(string): 将字符串转换为整数值。
# float(string): 将字符串转换为浮点数（小数）值。
age = input("How old are you? ")
age = int(age)
print(type(age), type(int(age)))
pi = float(input("What's the value of pi? "))


# While 循环
# 不断运行 while 语句块中的代码，直到给定的条件为假
# break 关键字: 退出整个循环语句块的执行。
# continue 关键字: 跳过当前循环中余下代码的执行。
current_number = 0
while True:
    current_number += 1
    if current_number > 5:
        break
    if current_number % 2 == 0:
        continue
    print(current_number)