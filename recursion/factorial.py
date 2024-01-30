def rec_factorial(n):
    if n == 1:
        return n
    else:
        return n * rec_factorial(n - 1)


x = int(input())
print(rec_factorial(x))
