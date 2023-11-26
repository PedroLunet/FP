def add(num1, num2):
    s1 = num1.split(".")
    s2 = num2.split(".")

    s1[0] = s1[0].rjust(max(len(s1[0]), len(s2[0])), '0')[::-1]
    s2[0] = s2[0].rjust(max(len(s1[0]), len(s2[0])), '0')[::-1]
    
    s1[1] = s1[1].ljust(max(len(s1[1]), len(s2[1])), '0')[::-1]
    s2[1] = s2[1].ljust(max(len(s1[1]), len(s2[1])), '0')[::-1]

    result_integer = ""
    result_decimal = ""
    carry = 0

    for i in range(max(len(s1[1]), len(s2[1]))):
        digit_sum = int(s1[1][i]) + int(s2[1][i]) + carry
        result_decimal += str(digit_sum % 10)
        carry = digit_sum // 10

    for i in range(max(len(s1[0]), len(s2[0]))):
        digit_sum = int(s1[0][i]) + int(s2[0][i]) + carry
        result_integer += str(digit_sum % 10)
        carry = digit_sum // 10

    if carry:
        result_integer += str(carry)

    result_integer = result_integer[::-1]
    result_decimal = result_decimal[::-1]
    result = result_integer.lstrip('0')  # Remove leading zeros from the integer part
    if result_decimal != '0':
        result += "." + result_decimal

    return result

