my_array = [1, 5, 8, 3, 9, 11, 2]

############ Merge Sort ############
### Time Complexity of Merge sort O(nlog(n))
### Because using Recursion not nested loop
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergesort(leftHalf)
    sortedRight = mergesort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:]) 
    result.extend(right[j:])

    return result

############ Bubble Sort ############
### Time Complexity of Bubble sort O(n^2)
def Bubble(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

############ Selection Sort ############
### Time Complexity of Selection sort O(n^2)
def Selection(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        ### Shift ###
        min_value = arr.pop(min_index)
        arr.insert(i, min_value)

        ### Swape ###
        # arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

############ Insertion Sort ############
### Time Complexity of Insertion sort O(n^2)
def Insertion(arr):
    n = len(arr)
    for i in range(1, n):
        insert_index = i
        current_value = arr.pop(i)
        j = i - 1
        while j >= 0 and arr[j] > current_value:
            insert_index = j
            j -= 1
        # for j in range(i-1, -1, -1):
        #     if arr[j] > current_value:
        #         insert_index = j
        arr.insert(insert_index, current_value)
    return arr


print(mergesort(my_array))