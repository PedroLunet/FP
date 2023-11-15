n1 = int(input())
n2 = int(input())

n1_str = str(n1)
n2_str = str(n2)

result = ""

for i in range(len(n1_str)):
    result += n1_str[-(i + 1)] + n2_str[-(i + 1)]

result_num = int(result)

print(result_num)





