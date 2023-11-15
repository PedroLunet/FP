a = int(input())

res = 0 
result = 0

while a != 0:
    res = a
    a -= 1
    if res % 3 == 0 or res % 5 == 0:
        result = result + res


print(result)
