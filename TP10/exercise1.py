def square_odds(values):
    vlist = values.split(",")
    return ",".join([str(int(x) ** 2) for x in vlist if int(x) % 2 != 0])




print(square_odds("1,2,3,4,5,6,7,8,9"))

# 1,9,25,49,81
	
print(square_odds("2,4,6,8"))

#	

print(square_odds("115"))

# 13225

print(square_odds("1,2,3,5,7,11,13"))

# 1,9,25,49,121,169
