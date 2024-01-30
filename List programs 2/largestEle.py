lst = [2, 4, 6, 8]


def largest_ele(item):
    global max_num
    for i in item:
        max_num = item[0]
        if i > max_num:
            max_num = i
    return max_num

print(largest_ele(lst))
