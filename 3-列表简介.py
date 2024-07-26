# 列表的创建和元素访问
bikes = ['trek', 'redline', 'giant']
print(bikes)
print(bikes[0])  # 索引从 0 开始，第一个元素的索引是 0
print(bikes[2], bikes[-1])


# 修改、添加和删除元素
# lst[idx] = val: 修改列表中指定索引的元素
bikes = ['trek']
bikes[0] = 'giant'
print(bikes)
# lst.append(val): 在列表的末尾添加新元素。
# lst.insert(idx, val): 在列表的指定位置上添加新元素。
bikes = []
bikes.append('redline')
bikes.insert(0, 'trek')
print(bikes)
# lst.pop([idx]) -> val: 删除并返回列表中指定索引（默认为末尾）的元素。
bikes = ['giant', 'trek', 'redline']
bikes.pop(0)        # 移除 'giant' 元素
print(bikes.pop())  # 移除 'redline' 元素并输出
print(bikes)
# del lst(idx): 删除列表中指定索引的元素。
# lst.remove(val): 删除列表中匹配到的第一个指定元素。
bikes = ['giant', 'redline', 'trek']
del bikes[0]          # 移除 'giant' 元素
bikes.remove('trek')  # 移除 'trek' 元素
print(bikes)


# 列表相关的常用方法
# lst.sort(): 永久修改原列表，对其中的元素进行排序。
# lst.reverse(): 永久修改原列表，对其中的元素进行翻转。
# sorted(lst) -> lst: 返回排序后的列表的副本。
# len(lst) -> num: 获取列表的元素个数。
nums = [9, 6, 1, 4, 2]
print(len(nums))
print(sorted(nums))
print(nums)  # 原列表不变
# 列表排序（默认正序）
nums.sort()
print(nums)
# 列表排序（指定倒序）
nums.sort(reverse=True)
print(nums)
nums.reverse()  # 翻转列表
print(nums)
