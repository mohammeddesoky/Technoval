### Recursion Tree with memorization ###
def Fibonacci(n, memo={}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = Fibonacci(n - 1, memo) + Fibonacci(n - 2, memo)
    return memo[n]

n = 9
print(Fibonacci(n))
## [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, .....]
## Time Complexity O(n)