def add(num1, num2):
    s1 = num1.split(".")
    s2 = num2.split(".")
    s1[0] = str(int(s1[0]))[::-1]
    s2[0] = str(int(s2[0]))[::-1]
    s1[1] = s1[1][::-1]
    s2[1] = s2[1][::-1]

    result_integer = ""
    result_decimal = ""
    carry = 0
    for i in range(max(len(s1[1]), len(s2[1]))):
        digit_sum = int(s1[1][i] if i < len(s1[1]) else 0) + int(s2[1][i] if i < len(s2[1]) else 0) + carry
        result_decimal += str(digit_sum % 10)
        carry = digit_sum // 10
    for i in range(max(len(s1[0]), len(s2[0]))):
        digit_sum = int(s1[0][i] if i < len(s1[0]) else 0) + int(s2[0][i] if i < len(s2[0]) else 0) + carry
        result_integer += str(digit_sum % 10)
        carry = digit_sum // 10


    if carry:
        result_integer += str(carry)

    result_integer = result_integer[::-1]
    result_decimal = result_decimal[::-1]
    result = result_integer + "." + result_decimal

    return result


    


print(add('123.456', '0.124'))
print(add('0123.40', '0.567'))
print(add('123.45', '1000.55'))
print(add('123456789.0', '0.00000000000001'))