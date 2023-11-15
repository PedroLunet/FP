low = int(input("Enter the lower bound: "))
up = int(input("Enter the upper bound: "))

result = []

for num in range(low, up + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if (num % i) == 0:
                is_prime = False
                break
        if is_prime:
            result.append(num)

prime_string = ' '.join(map(str, result))
print(f"Prime numbers between {low} and {up} are: {prime_string}")
