"""n = int(input())
i = 0

if n % 2 == 0:
    print("#" * n)
    while i < n - 2:
        print("#" * ((n - 2) // 2) + "00" + "#" * ((n - 2) // 2))
        i += 1
    print("#" * n) 


else:
    print("#" * n) 
    while i < n - 2:
        print("#" + "0" * (n - 2) + "#")
        i +=1
    print("#" * n) """

n = int(input())

if n % 2 == 0:
    # For even n
    for i in range(n):
        if i == n // 2 - 1 or i == n // 2:
            print("#" * (n // 2 - 1) + "00" + "#" * (n // 2 - 1))
        else:
            print("#" * n)
else:
    # For odd n
    for i in range(n):
        if i == n // 2:
            print("#" * (n // 2) + "0" + "#" * (n // 2))
        else:
            print("#" * n)




