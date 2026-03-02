def are_anagrams(s1, s2):
    freq1 = dict.fromkeys(list(s1), 0)
    freq2 = dict.fromkeys(list(s2), 0)
    for ch in s1:
        freq1[ch] += 1
    for ch in s2:
        freq2[ch] += 1
    return freq1 == freq2

s1 = 'abcdabcd'
s2 = 'aabbddcc'
print(are_anagrams(s1, s2))

### Time Complexity is O(n)