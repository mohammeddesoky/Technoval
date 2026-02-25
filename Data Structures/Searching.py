############ Linear Search ############
def Linear(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return f"Founded in index {i}"
    return "Not Founded"

############ Binary Search ############
## We use binary search when data is sorted only
def Binary(arr, target):
    arr = sorted(arr)
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return f"Founded in index {mid}"
        
        if target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
        
    return "Not Founded"


my_arr = [1, 4, 7, 54, 78, 2, 5]
target = 2
print(Binary(my_arr, target))