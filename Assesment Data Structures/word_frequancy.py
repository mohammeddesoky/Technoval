def word_frequency(text):
    freq = dict.fromkeys(list(text), 0)
    for ch in text:
        freq[ch] += 1
    return freq

text = 'ababcd'
print(word_frequency(text))