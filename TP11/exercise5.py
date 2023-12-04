def longest_prefix(words):
    if len(words) == 1:
        return words[0]
    else:
        mid = len(words) // 2
        left_prefix = longest_prefix(words[:mid])
        right_prefix = longest_prefix(words[mid:])
        return common_prefix(left_prefix, right_prefix)

def common_prefix(str1, str2):
    prefix = ""
    i = 0
    while i < len(str1) and i < len(str2) and str1[i] == str2[i]:
        prefix += str1[i]
        i += 1
    return prefix
