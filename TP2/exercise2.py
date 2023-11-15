n = int(input())
a1 = n - (n % 1000)
n = n - a1
a2 = n - (n % 100)
n = n - a2
a3 = n - (n % 10)
n = n - a3
print(a1)
print(a2)
print(a3)
print(n)