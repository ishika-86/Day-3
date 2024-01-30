def sumOfList(numList):
    if len(numList) == 1: return numList[0]
    return numList[0] + sumOfList(numList[1:])


lst = []

n = int(input())

for i in range(n):
    ele = int(input())
    lst.append(ele)

print(sumOfList(lst))
