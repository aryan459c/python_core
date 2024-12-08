

def is_palindrome(word):
    return word == word[::-1]
print(is_palindrome("level"))

"""=============================================================="""
def is_palindrome1(word):
    if word==word[::-1]:
        return "It is a palindrom"
    else:
        return "It is not a palindrom"

print(is_palindrome1('level'))

"""======================================="""
"""Using Loop"""
def is_palindrome3(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True

print(is_palindrome3("level"))

"""==========================="""

