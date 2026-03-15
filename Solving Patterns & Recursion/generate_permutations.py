### Backtracking ###
def permute(nums):
    result = []
    
    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for num in nums:
            if num in path:
                continue
            
            path.append(num)
            backtrack(path)
            path.pop()
    
    backtrack([])
    return result

nums = [1, 2, 3]
print(permute(nums))

## result: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]