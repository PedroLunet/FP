def sum(number):
    result = 0
    for i in range(1, number + 1):
        result += i
    return result

def var_numbers(number, precision = 2):
    result = 0
    mean = sum(number) / number
    for i in range(1, number + 1):
        aux = (i - mean)** 2
        result += aux
    result = result / number

    return round(result, precision)