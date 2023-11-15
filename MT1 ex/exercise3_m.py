import math

def approx_cos(x, n):
    result = 0
    for k in range(n):
        result += ((((-1) ** k) / ((math.factorial(2 * k)))) * (x ** (2 * k)))
    return round(result, 5)

    