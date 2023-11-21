def is_palindrome(s):
    return s == s[::-1]

def palindrome_index(s):
    if is_palindrome(s):
        return -1 
    
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            if is_palindrome(s[:i] + s[i + 1:]):
                return i
            elif is_palindrome(s[:len(s) - 1 - i] + s[len(s) - i:]):
                return len(s) - 1 - i
    
    return -1