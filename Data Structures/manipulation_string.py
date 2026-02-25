def reverse_string(s):
    return s[::-1]

def Palindrome(s):
    return s == s[::-1]

print(reverse_string("hello"))
print(Palindrome("racecar"))