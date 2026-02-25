def parentheses(text):
    if len(text) & 1:
        return False
    
    stack = []
    dic = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    for ch in text:
        if ch in '{[(':
            stack.append(ch)
        else:
            if stack.pop() != dic[ch] and not stack:
                return False
    return len(stack) == 0

txt = "[{()}]{}"
print(parentheses(txt))