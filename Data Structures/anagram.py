def anagram(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

###### Another Solution #####
def anagram(s1, s2):
    freq1 = {}
    freq2 = {}
    if len(s1) != len(s2):
        return False
    for ch in s1:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1

    for ch in s2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1

    if freq1 == freq2:
        return True
    else:
        return False

###### Another Solution with help LLM #####
def anagram(s1, s2):
    freq = {}
    if len(s1) != len(s2):
        return False
    for ch in s1:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    for ch in s2:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False
    return True



s1 = 'abcabc'
s2 = 'cbacba'
print(anagram(s1, s2))