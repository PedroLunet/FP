def validate_cc(number):
    number = str(number)
    number_list = list(number)
    number_list = number_list[::-1]
    checksum = 0
    aux = 0
    for i in range(len(number_list)):   
        if i % 2 == 1:
            aux = (int(number_list[i]) * 2)
            if aux > 9:
                aux = aux - 9
            checksum += aux
        else:
            checksum += int(number_list[i])
    if checksum % 10 == 0:
        return f"Card number {number} valid"
    else:
        return f"Card number {number} invalid (checksum {checksum % 10})"
