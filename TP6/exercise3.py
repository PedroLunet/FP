def change(amount):
    result = []
    while amount != 0:
        while amount >= 200:
            result.append(200)
            amount -= 200
        while amount >= 100:
            result.append(100)
            amount -= 100   
        while amount >= 50:
            result.append(50)
            amount -= 50
        while amount >= 20:
            result.append(20)
            amount -= 20
        while amount >= 10:
            result.append(10)
            amount -= 10
        while amount >= 5:
            result.append(5)
            amount -= 5
        while amount >= 2:
            result.append(2)
            amount -= 2
        while amount >= 1:
            result.append(1)
            amount -= 1
    return result

        
