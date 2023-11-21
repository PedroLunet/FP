def next_prime(number):
    while True:
        flag = False
        number += 1
        for i in range (2, number):
            if (number % i) == 0:
                flag = True
        if flag == False:
            return number
            
            
