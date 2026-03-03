def Binary_Search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return f'Found in index {mid}'
        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    
    return 'Not Founded' 

arr = [1, 2, 4, 5, 7, 9, 12, 45]
target = 12
print(Binary_Search(arr, target))

## Array must be sorted in Binary Search Because this depend on order and calculte half of data every step