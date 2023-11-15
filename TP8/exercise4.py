
def permutations(s):
    if len(s) == 0 or len(s) == 1:
        return [s]
    else:
        result = []
        for i in range(len(s)):
            perms = permutations(s[:i] + s[i+1:])
            for perm in perms:
                result.append(s[i] + perm)
        return result
