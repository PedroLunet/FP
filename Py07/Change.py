def change(money):
    result = {
        2.0: 0,
        1.0: 0, 
        0.5: 0, 
        0.2: 0, 
        0.1: 0, 
        0.05: 0, 
        0.02: 0, 
        0.01: 0
        }
    
    money = money * 100

    while money > 0:
        while money >= 200:
            result[2.0] += 1
            money -= 200
        while money >= 100:
            result[1.0] += 1
            money -= 100
        while money >= 50:
            result[0.5] += 1
            money -= 50
        while money >= 20:
            result[0.2] += 1
            money -= 20
        while money >= 10:
            result[0.1] += 1
            money -= 10
        while money >= 5:
            result[0.05] += 1
            money -= 5
        while money >= 2:
            result[0.02] += 1
            money -= 2
        while money >= 1:
            result[0.01] += 1
            money -= 1
    return result
