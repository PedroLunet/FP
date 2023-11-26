#Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

#Expected output:
#{'Ten': 10, 'Twenty': 20, 'Thirty': 30}

dict = {}

for i in range(len(keys)):
    dict[keys[i]] = values[i]

print(dict)

############################################ OTHER SOLUTIONS #######################################################

# res_dict = dict(zip(keys, values))
# print(res_dict)

#___________________________________________#

# res_dict = dict()
# for i in range(len(keys)):
#     res_dict.update({keys[i]: values[i]})
# print(res_dict)

#___________________________________________#
