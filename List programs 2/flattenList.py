import itertools as it

org_lst = [[2, 3, 4], [5, 6, 7], [8, 9]]
new_lst = list(it.chain(*org_lst))
print(new_lst)