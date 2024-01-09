def union_with(combine, dict1: dict, dict2: dict):
    def handle(key):
        if key in dict1 and key in dict2:
            value1 = dict1[key]
            value2 = dict2[key]
            result = combine(value1, value2)
            return result
        elif key in dict1:
            return dict1[key]
        elif key in dict2:
            return dict2[key]
        
    keys = dict1.keys() | dict2.keys()         
    result = {key: handle(key) for key in keys} 
    return result


print(sorted(union_with(lambda x,y:x+y, {'a':1, 'b':2}, {'a':3, 'c':4}).items()))
#[('a', 4), ('b', 2), ('c', 4)]
print(sorted(union_with(max, {'a':3, 'b':1, 'c':0}, {'a':1, 'b':3, 'c':2, 'd':5}).items()))
#[('a', 3), ('b', 3), ('c', 2), ('d', 5)]
print(sorted(union_with(lambda x,y:x-y, {'a':3, 'b':2, 'c':3}, {'a':2, 'b':1}).items()))
#[('a', 1), ('b', 1), ('c', 3)]
print(sorted(union_with(lambda x,y:x+y, {1:'a', 2:'b', 3:'c'}, {1:'y', 2:'x', 4:'z'}).items()))
#[(1, 'ay'), (2, 'bx'), (3, 'c'), (4, 'z')]