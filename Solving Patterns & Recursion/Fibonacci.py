### Recursion Tree ###
def Fibonacci(n):
    if n <= 1:
        return n
    return Fibonacci(n - 1) + Fibonacci(n - 2)

n = 10
print(Fibonacci(n))
## [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, .....]
## Time Complexity O(2^n)