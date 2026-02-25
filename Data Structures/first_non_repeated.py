def first_non_repeated(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    for x, y in freq.items():
        if y == 1:
            return x
    return None

s = 'aabbcccvassddwertyu'
print(first_non_repeated(s))