def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


nTerms = int(input())
if nTerms > 0:
    for i in range(nTerms):
        print(fibonacci_recursive(i))
else:
    print("invalid input")
