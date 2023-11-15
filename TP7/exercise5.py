def next_middle_square(number, digits):
   """Compute the next pseudo-random using the 
      middle square algorithm and the given number of digits."""
   k = digits // 2         # half of the number of digits
   square = number*number  # compute the square
   middle = (square // (10**k)) % (10**digits)   # extract middle part
   return middle
def cycle_length(number, digits):
    conjunto=set()
    res = 0
    while res == 0:
        number=next_middle_square(number, digits)
        if number in conjunto:
            res=1
            x = number
            number=next_middle_square(number, digits)
        else:
            conjunto.add(number)
    while number != x:
        number=next_middle_square(number, digits)
        res+=1
    return res


