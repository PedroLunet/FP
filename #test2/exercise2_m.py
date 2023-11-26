def next_prime(number):
    while True:
        number += 1
        if isprime(number):
            return number

def isprime(n):
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
    return flag


print(next_prime(10))
#    11
print(next_prime(13))
#    17
print(next_prime(26))
#   29
print(next_prime(450))
#    457
print(next_prime(600))
#    601
print(next_prime(4374))
#    4391
print(next_prime(3150))
#    3163
print(next_prime(202500))
#    202519