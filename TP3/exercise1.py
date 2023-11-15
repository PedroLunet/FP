num = int(input())
for i in range(1, 11):
    if i == num:
        print(str(num) + " ^ 2 = " + str(num**2))
        break
    else:
        print(str(num) + " x " + str(i) + " = " + str(num * i))