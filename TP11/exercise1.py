"""
Created on Thu 30 nov 2023 09:49:15 WET

@author: ChatGPT (prompt: "Write a Python function merge(xs, ys) to merge 
sorted lists xs and ys. Return a sorted result.")
"""
def merge(xs, ys):
    result = []
    i = j = 0
    while i < len(xs) and j < len(ys):
        if xs[i] < ys[j]:
            result.append(xs[i])
            i += 1
        else:
            result.append(ys[j])
            j += 1

    # Add the remaining elements from both lists, if any
    result.extend(xs[i:])
    result.extend(ys[j:])

    return result

def msort(xs):
    if len(xs) <= 1:
        return xs
    
    l = len(xs)
    h1 = xs[:l//2]
    h2 = xs[l//2:]
    return merge(msort(h1), msort(h2))


print(msort([3, 2, 1, 4]))

#[1, 2, 3, 4]

print(msort([3, 3]))

#[3, 3]

print(msort([7, 3, 1, 2, 4, 5, 6]))

#[1, 2, 3, 4, 5, 6, 7]

print(msort([7, 3, 1, 2, 4, 5, 6, 3, 2, 5, 6, 1]))

#[1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7]