def check_friendly(number_one, number_two):
    if number_one == number_two:
        return f"identical numbers: {number_one}"
    else:
        #Calculate the sum of the divisors of number_one excluding itself
        sd1 = 0
        sd2 = 0
        for i in range(1, number_one):
            if number_one % i == 0:
                sd1 += i
        #Calculate the sum of the divisors of number_two excluding itself
        for i in range(1, number_two):
            if number_two % i == 0:
                sd2 += i
        if sd1 == number_two and sd2 == number_one:
            return f"{number_one} and {number_two} are friendly"
        elif sd1 != number_two:
            return f"sum of divisors of {number_one} is not {number_two}"
        else:
            return f"sum of divisors of {number_two} is not {number_one}"
        