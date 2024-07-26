# 循环遍历列表
bikes = ['trek', 'redline']
for bike in bikes:
    print(bike.title())


# 创建数值列表和列表推导式
# range([start,] end [,step]): 生成可迭代的数值列表的表示。
# max(lst)/min(lst)/sum(lst): 对数值列表执行简单的统计计算。
print(range(2))
print(list(range(2)))

squares = []
for value in range(2, 5):
    squares.append(value ** 2)

squares_comp = [value ** 2 for value in range(2, 5)]
print(squares == squares_comp)  # 推导式会创建相同的元素
print(squares)
print(min(squares), max(squares), sum(squares))


# 创建列表切片
bikes = ['trek', 'redline', 'giant']
print(bikes[1:])
print(bikes[:-1])
print(bikes[0:1])
bikes_copy = bikes[:]
# 对副本的浅拷贝操作，这里不影响原列表
bikes_copy.reverse()
print(bikes)
print(bikes_copy)


# 元组的定义和遍历
dimensions = (200, 50)
for value in dimensions:
    print(value)
# 元组无法修改，但变量可以被重新赋值
dimensions = (300, 100)
print(dimensions)
dimensions = 100
print(dimensions)