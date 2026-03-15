## With two pointers
## Time O(n), Space O(1)
def two_sum(arr, target):
    arr = sorted(arr)
    left = 0
    right = len(arr) - 1
    while left <= right:
        summ = arr[left] + arr[right]
        if target == summ:
            return f"Found ({arr[left]}, {arr[right]})"
        elif target > summ:
            left += 1
        else:
            right -= 1
    return 'Not Found'

arr = [0, 1, 2, 3, 4, 5]
target = 9
print(two_sum(arr, target))

## With Naive Method
## Time O(n^2), Space O(1)
def two_sum_naive(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return f"Found ({arr[i]}, {arr[j]})"
    return 'Not Found'

arr = [0, 1, 2, 3, 4, 5]
target = 9
print(two_sum_naive(arr, target))