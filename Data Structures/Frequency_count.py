def Frequency_count(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

numbers = [1, 1, 2, 3, 1, 3, 4, 6, 2, 6]
print(Frequency_count(numbers))

s = 'aabbccvvbabb'
print(Frequency_count(s))
    