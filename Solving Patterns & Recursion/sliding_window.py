###   Sliding Window   ###
### Time O(n), Space O(1) ###
def MaxSum(arr, k):
    n = len(arr)
    if k >= n:
        print("Invalid")
        return -1
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

arr = [0, 1, 2, 3, 4, 5, 6]
k = 3
print(MaxSum(arr, k))

###   Naive Method   ###
### Time O(n * k), Space O(1)
def max_naive(arr, k):
    n = len(arr)
    max_sum = float("-inf")
    for i in range(n - k + 1):
        current_sum = 0
        for j in range(k):
            current_sum += arr[i + j]
        max_sum = max(max_sum, current_sum)

    return max_sum

arr = [0, 1, 2, 3, 4, 5, 6]
k = 3
print(max_naive(arr, k))