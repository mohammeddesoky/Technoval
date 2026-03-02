def valid_parentheses(txt):
    stack = []
    pair = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for ch in txt:
        if ch in '{([':
            stack.append(ch)
        elif not stack or stack.pop() != pair[ch]:
            return False
    return not stack

text = '([{[([])]}])'
print(valid_parentheses(text))