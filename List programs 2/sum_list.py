lst = []

n = int(input())
for i in range(n):
    ele = int(input())
    lst.append(ele)


def sum_list(lst):
    sum_nums: int = 0
    for i in lst:
        sum_nums += i
    return sum_nums


print(sum_list(lst))
