def word_frequency_count(txt):
    words = txt.split()
    freq = dict.fromkeys(words, 0)
    for word in words:
        if word in freq:
            freq[word] += 1
    return freq

###### Another Solution #####
def word_frequency_count(txt):
    words = txt.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

txt = 'apple banana apple orange banana apple'
print(word_frequency_count(txt))