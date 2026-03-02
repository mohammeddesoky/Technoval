def first_unique_char(txt):
    freq = dict.fromkeys(list(txt), 0)
    for ch in txt:
        freq[ch] += 1

    for i, ch in enumerate(txt):
        if freq[ch] == 1:
            return i
    return -1

text = 'abababcssddv'
print(first_unique_char(text))