# 字典的创建和访问
alien = {'color': 'green', 'points': 5}
print(alien['color'], alien.get('color'))


# 修改、添加和删除键值
alien = {'color': 'green', 'points': 5}
alien['color'] = 'red'
alien['position'] = (0, 25)
print(alien)
# del d[key]: 根据键删除指定的键值对。
# d.pop(key) -> val: 根据键删除指定的键值对，返回键对应的值。
d = {'a': 1, 'b': 2, 'c': 3}
del d['a']
print(d.pop('c'))
print(d)


# 字典的常用方法
# d.items(): 返回所有键值对的元组视图。
# d.keys()/d.values(): 返回所有键/值的列表视图。
# len(d): 获取字典的键值对的组数。
favorites = {'jen': 'python', 'edward': 'rust'}
print(len(favorites))
for name, language in favorites.items():
    print(f'{name} loves {language}')

print(list(favorites.keys()))
print(list(favorites.values()))


# 字典推导式
squares = {x: x ** 2 for x in range(4)}
keys, vals = [0, 1, 2, 3], [0, 1, 4, 9]
squares_zip = {key: val
               for key, val in zip(keys, vals)}

print(squares == squares_zip, squares)
