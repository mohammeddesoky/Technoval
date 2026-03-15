def length_of_longest_substring(s):
    left = 0
    seen = {}
    max_length = 0
    
    for right in range(len(s)):
        char = s[right]
        
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        
        seen[char] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length

s = 'ababcc'
print(length_of_longest_substring(s))