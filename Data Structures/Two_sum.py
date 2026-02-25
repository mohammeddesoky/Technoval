def two_sum(nums, target):
    dic = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in dic:
            index = f'Index {[dic[complement], i]}'
            value = f'Values {[complement, nums[i]]}'
            return index + '\n' + value
        
        dic[num] = i
    
    return 'Not Found'

nums = [3, 4, 7, 8, 1, 3, 5]
target = 15
print(two_sum(nums, target))