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
