# 函数定义
# 形参 color 有默认值
def describe_pet(animal, name, color='yellow'):
    """显示宠物的信息"""
    print(f"My {animal}'s name is {name}, color is {color}.")


describe_pet('hamster', 'harry')
describe_pet(name='willie', color='black', animal='dog')


# 函数的返回值
def add_if_same_or_sub(x, y):
    if x == y:
        return x + y
    return x - y

val1 = add_if_same_or_sub(5, 2)
val2 = add_if_same_or_sub(2, 2)
print(val1, val2)


# 不定长参数
# *args: 以一个星号为前缀，将接受一个包含多余位置参数的元组。
# **kwargs: 以两个星号为前缀，将接受一个包含多余关键字参数的字典。
def func(*args, **kwargs):
    print(f"args: {args}\nkwargs: {kwargs}")

func(1, 2, k='v')
