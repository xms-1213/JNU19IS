import random
#参数min_or_max:0是求最小值，1是求最大值
def get_min_or_max_number(numbers_array = [], min_or_max = 0):
    if min_or_max == 0:
        _min = 0
        for i in numbers_array:
            if i < _min:
                _min = i
        return i
    if min_or_max == 1:
        _max = 0
        for i in numbers_array:
            if i > _max:
                _max = i
        return i
    

test_numbers = []
for i in range(0, 10):
    new_number = random.randint(0, 100)
    test_numbers.append(new_number)

print("测试数据：" + str(test_numbers))
min_number = get_min_or_max_number(test_numbers, 0)
max_number = get_min_or_max_number(test_numbers, 1)
print("最大数：" + str(min_number))
print("最小数：" + str(max_number))